"""solution of adv_2022_12"""

import math
import collections


def parse_input(in_str):
    """returns the height_data, start_pos and end_pos"""
    start_pos = None
    end_pos = None

    def _proc_single_line(line_num, in_line):
        nonlocal start_pos
        nonlocal end_pos
        res = []
        for char_num, cur_char in enumerate(list(in_line)):
            if cur_char == "S":
                assert start_pos is None
                start_pos = (char_num, line_num)
                res.append(ord("a"))
            elif cur_char == "E":
                assert end_pos is None
                end_pos = (char_num, line_num)
                res.append(ord("z"))
            else:
                res.append(ord(cur_char))
        return tuple(res)

    height_data = tuple(_proc_single_line(*_) for _ in enumerate(in_str.splitlines()))
    parse_res = collections.namedtuple(
        "parse_res", ["height_data", "start_pos", "end_pos"]
    )
    return parse_res(height_data, start_pos, end_pos)


def _is_in_range(height_data, in_pos):
    x_pos, y_pos = in_pos
    return 0 <= y_pos < len(height_data) and 0 <= x_pos < len(height_data[y_pos])


def get_height(height_data, in_pos):
    """
    Returns the height at given position.
    If position is outside the range, it returns -1.
    """
    assert _is_in_range(height_data, in_pos)
    x_pos, y_pos = in_pos
    return height_data[y_pos][x_pos]


def _shift_pos(in_pos, in_shift):
    return tuple(a + b for (a, b) in zip(in_pos, in_shift))


def _gen_valid_neighbours(height_data, in_pos):
    for _ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cur_pos = _shift_pos(in_pos, _)
        if _is_in_range(height_data, cur_pos):
            yield cur_pos


def gen_candidates_a(height_data, in_pos):
    """yields  positions which can be visited in part a"""
    in_height = get_height(height_data, in_pos)
    for _ in _gen_valid_neighbours(height_data, in_pos):
        if in_height + 1 >= get_height(height_data, _):
            yield _


def gen_candidates_b(height_data, in_pos):
    """yields  positions which can be visited in part b"""
    in_height = get_height(height_data, in_pos)
    for _ in _gen_valid_neighbours(height_data, in_pos):
        if in_height - 1 <= get_height(height_data, _):
            yield _


def _find_dist(start_pos, gen_candidates_fun, is_end_fun):
    data = [(start_pos, 0)]
    best_len = math.inf
    visited = set()
    while data:
        cur_pos, cur_len = data.pop(0)
        if is_end_fun(cur_pos):
            best_len = min(best_len, cur_len)
        elif cur_pos not in visited:
            visited.add(cur_pos)
            for _ in gen_candidates_fun(cur_pos):
                data.append((_, cur_len + 1))
    return best_len


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    return _find_dist(
        data.start_pos,
        lambda p: gen_candidates_a(data.height_data, p),
        lambda x: x == data.end_pos,
    )


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    return _find_dist(
        data.end_pos,
        lambda p: gen_candidates_b(data.height_data, p),
        lambda x: get_height(data.height_data, x) == ord("a"),
    )
