"""solution of adv_2022_17"""

import itertools
import collections
import copy


def _most_left(in_shape):
    return min((_[0] for _ in in_shape), default=0)


def _most_right(in_shape):
    return max((_[0] for _ in in_shape), default=0)


def _most_down(in_shape):
    return min((_[1] for _ in in_shape), default=0)


def _most_up(in_shape):
    return max((_[1] for _ in in_shape), default=0)


def _find_corner(in_shape):
    return _most_left(in_shape), _most_down(in_shape)


def _shift_pos(in_pos, in_shift):
    return tuple(p + s for (p, s) in zip(in_pos, in_shift))


def _shift_shape(in_shape, in_shift):
    return frozenset(_shift_pos(_, in_shift) for _ in in_shape)


def _normalise(in_shape):
    corner = _find_corner(in_shape)
    shift = tuple(-_ for _ in corner)
    return _shift_shape(in_shape, shift)


def _parse_single_block(in_str):
    res = []
    for y_pos, cur_row in enumerate(in_str.splitlines()):
        for x_pos, cur_char in enumerate(cur_row):
            if cur_char == "#":
                res.append((x_pos, -y_pos))
            else:
                assert cur_char == "."
    return _normalise(res)


def parse_blocks(in_str):
    """returns a tuple of frozensets representng blocks"""
    return tuple(_parse_single_block(_.strip()) for _ in in_str.split("\n\n"))


def parse_input(in_str):
    """parses the input into list of moves"""

    def _proc_single_char(in_char):
        assert in_char in {"<", ">"}
        return in_char

    return tuple(_proc_single_char(_) for _ in in_str.strip())


def _is_valid(in_rocks, in_shape):
    if _most_left(in_shape) < 0:
        return False
    if _most_right(in_shape) >= 7:
        return False
    if _most_down(in_shape) < 0:
        return False

    if in_rocks and in_rocks.intersection(in_shape):
        return False

    return True


def _get_left_or_right_shft(in_move_char):
    return {"<": (-1, 0), ">": (1, 0)}[in_move_char]


def _move_to_start_pos(in_rocks, in_shape):
    rocks_top = _most_up(in_rocks) if in_rocks else -1
    shape_bottom = _most_down(in_shape)
    assert shape_bottom <= 0
    return _shift_shape(in_shape, (2, rocks_top + 3 - shape_bottom + 1))


def drop_single(in_rocks, shape, gen_moves):
    """returns the new rocks confiuration after dropping a single block"""
    shape = _move_to_start_pos(in_rocks, shape)
    res = None
    for _ in gen_moves:
        tmp_shape = _shift_shape(shape, _get_left_or_right_shft(_))
        if _is_valid(in_rocks, tmp_shape):
            shape = tmp_shape
        tmp_shape = _shift_shape(shape, (0, -1))
        if _is_valid(in_rocks, tmp_shape):
            shape = tmp_shape
        else:
            res = in_rocks.union(shape)
            break
    return res


with open("solutions/data_adv_2022_17_blocks.txt", "r", encoding="utf-8") as f:
    _BLOCKS = parse_blocks(f.read())

_MAX_BLOCK_HEIGHT = max(_most_up(_) for _ in _BLOCKS)


def _get_top_of_column(rocks, in_x):
    return max((_[1] for _ in rocks if _[0] == in_x), default=0)


def _optimise_rocks(in_rocks):
    limit = (
        min(_get_top_of_column(in_rocks, _) for _ in range(0, 7))
        - _MAX_BLOCK_HEIGHT
        - 1
    )
    return frozenset(_ for _ in in_rocks if _[1] >= limit)


def _simulate(in_rocks, generators, total_number_of_blocks, cache):
    rocks = copy.deepcopy(in_rocks)

    for _ in range(total_number_of_blocks):
        block = next(generators.blocks)
        initial_top = _most_up(rocks)
        initial_normalised_rocks = _normalise(rocks)
        rocks = drop_single(rocks, block, generators.moves)
        rocks = _optimise_rocks(rocks)
        gained_height = _most_up(rocks) - initial_top
        normalised_rocks = _normalise(rocks)
        if normalised_rocks not in cache.gained_height:
            cache.gained_height[normalised_rocks] = gained_height
        else:
            assert cache.gained_height[normalised_rocks] == gained_height

        if initial_normalised_rocks not in cache.next_state:
            cache.next_state[initial_normalised_rocks] = normalised_rocks
        else:
            assert cache.next_state[initial_normalised_rocks] == normalised_rocks

    return rocks


def _compute_cycle_data(in_rocks, cache):
    total_gained_height = cache.gained_height[in_rocks]
    cur_rocks = cache.next_state[in_rocks]
    cycle_length = 1
    while cur_rocks != in_rocks:
        total_gained_height += cache.gained_height[cur_rocks]
        cur_rocks = cache.next_state[cur_rocks]
        cycle_length += 1

    CycleData = collections.namedtuple("CycleData", ["gained_height", "cycle_length"])
    return CycleData(total_gained_height, cycle_length)


def _compute_gained_height(in_rocks, cache, number_of_iterations):
    cur_rocks = copy.deepcopy(in_rocks)
    res = 0
    for _ in range(number_of_iterations):
        res += cache.gained_height[cur_rocks]
        cur_rocks = cache.next_state[cur_rocks]
    return res


def _calculate_height(in_str, total_number_of_blocks):
    moves = parse_input(in_str)
    rocks = frozenset()
    generators = collections.namedtuple("Generators", ["blocks", "moves"])(
        itertools.cycle(_BLOCKS), itertools.cycle(moves)
    )
    cache = collections.namedtuple("Cache", ["gained_height", "next_state"])({}, {})
    number_of_blocks = 0

    while (
        len(cache.gained_height) >= number_of_blocks
        and len(cache.gained_height) >= number_of_blocks
    ):
        d_num = 150
        rocks = _simulate(rocks, generators, d_num, cache)
        number_of_blocks += d_num
    assert number_of_blocks < total_number_of_blocks
    cycle_data = _compute_cycle_data(_normalise(rocks), cache)
    blocks_left = total_number_of_blocks - number_of_blocks + 1
    remaining_blocks = blocks_left % cycle_data.cycle_length
    number_of_periods = (blocks_left - remaining_blocks) // cycle_data.cycle_length

    return (
        _most_up(rocks)
        + number_of_periods * cycle_data.gained_height
        + _compute_gained_height(_normalise(rocks), cache, remaining_blocks)
        + 1
    )


def solve_a(in_str):
    """returns the solution for part_a"""
    return _calculate_height(in_str, 2022)


def solve_b(in_str):
    """returns the solution for part_b"""
    return _calculate_height(in_str, 1000000000000)
