"""solution of adv_2022_24"""

import math
import collections


def _lcm(in_a, in_b):
    return (in_a * in_b) // math.gcd(in_a, in_b)


def _make_shift_mod(in_pos, in_shift, in_limits):
    return tuple((p + s) % m for (p, s, m) in zip(in_pos, in_shift, in_limits))


def _make_shift(in_pos, in_shift):
    return tuple(sum(_) for _ in zip(in_pos, in_shift))


class Blizzard:
    def __init__(self, dir_name):
        self.dir = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[dir_name]


def new_blizzard_pos(in_size, in_pos, in_blizzard):
    return _make_shift_mod(in_pos, in_blizzard.dir, in_size)


def _compute_new_positions(in_size, in_cur_positions, in_blizzard_types):
    return tuple(
        new_blizzard_pos(in_size, pos, bliz)
        for pos, bliz in zip(in_cur_positions, in_blizzard_types)
    )


def generate_all_blizzard_positions(in_size, in_blizzards):
    max_age = _lcm(*in_size)
    res = []
    cur_positions = tuple(_[0] for _ in in_blizzards)
    blizzard_types = [_[1] for _ in in_blizzards]
    for cur_age in range(max_age):
        res.append(frozenset(cur_positions))
        cur_positions = _compute_new_positions(in_size, cur_positions, blizzard_types)
    assert frozenset(cur_positions) == res[0]
    return tuple(res)


class BlizzardPositions:
    def __init__(self, in_positions):
        self._positions = in_positions

    def is_empty(self, in_age, in_pos):
        return in_pos not in self._positions[in_age % len(self._positions)]


def _get_start_pos():
    return (0, -1)


def _get_end_pos(in_size):
    return _make_shift(in_size, (-1, 0))


def position_candidates(in_size, in_pos):
    if in_pos == _get_start_pos():
        return [(0, 0), in_pos]

    res = [in_pos]
    for _ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = _make_shift(in_pos, _)
        if 0 <= new_pos[0] < in_size[0] and 0 <= new_pos[1] < in_size[1]:
            res.append(new_pos)

    if in_pos == (0, 0):
        res.append(_get_start_pos())
    elif in_pos == _make_shift(in_size, (-1, -1)):
        res.append(_get_end_pos(in_size))

    return res


def _to_key(in_pos, in_time):
    return (in_pos, in_time)


def find_minimal_time(in_size, blizzard_positions, start_pos, target_pos, start_time):
    known = set()
    active = [_to_key(start_pos, 0)]
    best_time = math.inf
    max_x = 0
    max_y = 0
    while active:
        cur_key = active.pop(0)
        if cur_key in known:
            continue
        cur_pos, cur_time = cur_key
        if cur_pos == target_pos:
            best_time = min(best_time, cur_time)
            continue

        if cur_time > best_time:
            continue

        max_x = max(max_x, cur_pos[0])
        max_y = max(max_y, cur_pos[1])

        assert blizzard_positions.is_empty(cur_time + start_time, cur_pos)
        known.add(cur_key)

        for _ in position_candidates(in_size, cur_pos):
            if blizzard_positions.is_empty(cur_time + 1 + start_time, _):
                active.append(_to_key(_, cur_time + 1))
    return best_time


def parse_input(in_str):
    """parses the input into..."""

    lines = in_str.splitlines()
    height = len(lines) - 2
    width = len(lines[0]) - 2
    assert lines[0][1] == "."
    assert set(lines[0][0] + lines[0][2:]) == {"#"}
    assert lines[-1][-2] == "."
    assert set(lines[-1][0:-2] + lines[-1][-1]) == {"#"}

    blizzards = []
    for y_pos, cur_row in enumerate(lines[1:-1]):
        assert cur_row[0] == "#" and cur_row[-1] == "#" and len(cur_row) - 2 == width
        for x_pos, cur_char in enumerate(cur_row[1:-1]):
            if cur_char != ".":
                blizzards.append(((x_pos, y_pos), Blizzard(cur_char)))
    return collections.namedtuple("ParseRes", ["size", "blizzards"])(
        (width, height), blizzards
    )


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    bliz_positions = BlizzardPositions(
        generate_all_blizzard_positions(data.size, data.blizzards)
    )
    return find_minimal_time(
        data.size, bliz_positions, _get_start_pos(), _get_end_pos(data.size), 0
    )


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    bliz_positions = BlizzardPositions(
        generate_all_blizzard_positions(data.size, data.blizzards)
    )

    time_a = find_minimal_time(
        data.size, bliz_positions, _get_start_pos(), _get_end_pos(data.size), 0
    )
    time_b = find_minimal_time(
        data.size, bliz_positions, _get_end_pos(data.size), _get_start_pos(), time_a
    )
    time_c = find_minimal_time(
        data.size,
        bliz_positions,
        _get_start_pos(),
        _get_end_pos(data.size),
        time_a + time_b,
    )
    return time_a + time_b + time_c
