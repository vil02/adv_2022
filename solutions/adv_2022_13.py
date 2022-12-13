"""solution of adv_2022_13"""

import functools
import itertools


def _parse_element(in_str):
    if not in_str:
        return None
    if in_str[0] == "[":
        assert in_str[-1] == "]"
        return parse_list(in_str)
    return int(in_str)


def split_lists(in_str):
    """splist string into pieces soccesponsing to its entries"""
    cur_counter = 0
    res = []
    last_pos = 0
    for (num, cur_char) in enumerate(in_str):
        if cur_char == "[":
            cur_counter += 1
        elif cur_char == "]":
            cur_counter -= 1
        if cur_counter == 0 and cur_char == ",":
            res.append(in_str[last_pos:num])
            last_pos = num + 1
    assert cur_counter == 0
    res.append(in_str[last_pos:])
    return res


def parse_list(in_str):
    """parses in_str into list"""
    assert in_str[0] == "[" and in_str[-1] == "]"
    res = (_parse_element(_) for _ in split_lists(in_str[1:-1]))
    return [_ for _ in res if _ is not None]


def parse_input(in_str):
    """parses the input into list of pairs"""

    def _proc_single_block(in_block):
        res = tuple(parse_list(_) for _ in in_block.split("\n"))
        assert len(res) == 2
        return res

    return tuple(_proc_single_block(_.strip()) for _ in in_str.split("\n\n"))


def _is_in_order_ints(int_a, int_b):
    assert isinstance(int_a, int) and isinstance(int_b, int)
    if int_a < int_b:
        return 1
    if int_a == int_b:
        return 0
    return -1


def _is_in_order_lists(left, right):
    if not left and right:
        return 1
    if left and not right:
        return -1
    if not left and not right:
        return 0
    cur_res = is_in_order(left[0], right[0])
    if cur_res == 0 and left and right:
        return is_in_order(left[1:], right[1:])
    return cur_res


def is_in_order(left, right):
    """returns 1 if left is before right"""
    if isinstance(left, int) and isinstance(right, int):
        return _is_in_order_ints(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return _is_in_order_lists(left, right)
    if isinstance(left, int) and isinstance(right, list):
        return is_in_order([left], right)

    assert isinstance(left, list) and isinstance(right, int)
    return is_in_order(left, [right])


def _to_index(in_num):
    return in_num + 1


def solve_a(in_str):
    """returns the solution for part_a"""
    pairs = parse_input(in_str)
    return sum(_to_index(num) for (num, _) in enumerate(pairs) if is_in_order(*_) == 1)


def _sort_is_in_order(left, right):
    return -is_in_order(left, right)


def solve_b(in_str):
    """returns the solution for part_b"""
    div_a = [[2]]
    div_b = [[6]]
    pairs = parse_input(in_str) + ((div_a, div_b),)
    pairs = sorted(itertools.chain(*pairs), key=functools.cmp_to_key(_sort_is_in_order))
    return _to_index(pairs.index(div_a)) * _to_index(pairs.index(div_b))
