"""solution of adv_2022_23"""

import collections
import math


def _to_pos(in_x, in_y):
    return (in_x, in_y)


def parse_input(in_str):
    """parses the input into a frozenset of positions"""

    res = set()
    for y_pos, row in enumerate(in_str.splitlines()):
        for x_pos, char in enumerate(row):
            if char == "#":
                res.add(_to_pos(x_pos, y_pos))
            else:
                assert char == "."
    return frozenset(res)


def _make_shift(in_pos, in_shift):
    return tuple(sum(_) for _ in zip(in_pos, in_shift))


def _get_dirs_dict():
    res = {
        "N": (0, -1),
        "S": (0, 1),
        "W": (-1, 0),
        "E": (1, 0),
    }
    res["NE"] = _make_shift(res["N"], res["E"])
    res["NW"] = _make_shift(res["N"], res["W"])
    res["SE"] = _make_shift(res["S"], res["E"])
    res["SW"] = _make_shift(res["S"], res["W"])
    assert len(res) == 8
    return res


def _get_dir(in_dir_name):
    return _get_dirs_dict()[in_dir_name]


def get_dir_name(in_num):
    """returns the direction name based on a direction number"""
    return {0: "N", 1: "S", 2: "W", 3: "E"}[in_num]


def _get_all_neighbours(in_pos):
    return tuple(_make_shift(in_pos, _) for _ in _get_dirs_dict().values())


def _get_similar_dirs(in_dir_name):
    return {
        "N": ("N", "NE", "NW"),
        "S": ("S", "SE", "SW"),
        "W": ("W", "NW", "SW"),
        "E": ("E", "NE", "SE"),
    }[in_dir_name]


def _are_all_empty(in_pos, in_dir_names, in_elves_positions):
    return all(
        _make_shift(in_pos, _get_dir(_)) not in in_elves_positions for _ in in_dir_names
    )


class Elf:
    """represents a moving elf"""

    def __init__(self, in_pos):
        self.pos = in_pos
        self.new_pos = None

    def propose_pos(self, in_elves_positions, in_dir_names):
        """makes a position proposal"""
        self.new_pos = None
        neighbours = _get_all_neighbours(self.pos)
        if all(_ not in in_elves_positions for _ in neighbours):
            return self.new_pos

        for cur_dir_name in in_dir_names:
            if _are_all_empty(
                self.pos, _get_similar_dirs(cur_dir_name), in_elves_positions
            ):
                self.new_pos = _make_shift(self.pos, _get_dir(cur_dir_name))
                break
        return self.new_pos

    def move(self):
        """performs a move"""
        assert self.new_pos is not None
        self.pos = self.new_pos
        self.new_pos = None


def single_round(elves, dir_names):
    """makes a single round of moves"""
    new_positions = {}
    elves_positions = {_.pos for _ in elves}

    for cur_elf in elves:
        new_pos = cur_elf.propose_pos(elves_positions, dir_names)
        if new_pos is not None:
            new_positions[new_pos] = new_positions.get(new_pos, 0) + 1

    any_moved = False
    for cur_elf in elves:
        if cur_elf.new_pos is not None and new_positions[cur_elf.new_pos] == 1:
            cur_elf.move()
            any_moved = True

    dir_names.append(dir_names.pop(0))
    return any_moved


def _update_bound(in_fun, in_bound, in_pos):
    return tuple(in_fun(b, p) for b, p in zip(in_bound, in_pos))


def _calculate_bounds(in_positions):
    mins = (math.inf, math.inf)
    maxs = (-math.inf, -math.inf)
    for _ in in_positions:
        mins = _update_bound(min, mins, _)
        maxs = _update_bound(max, maxs, _)

    return collections.namedtuple("Bounds", ["mins", "maxs"])(mins, maxs)


def solve_a(in_str):
    """returns the solution for part_a"""
    elves = [Elf(_) for _ in parse_input(in_str)]
    dir_names = [get_dir_name(_) for _ in range(4)]
    for _ in range(10):
        single_round(elves, dir_names)
    positions = [_.pos for _ in elves]
    bounds = _calculate_bounds(positions)

    return (bounds.maxs[0] - bounds.mins[0] + 1) * (
        bounds.maxs[1] - bounds.mins[1] + 1
    ) - len(elves)


def solve_b(in_str):
    """returns the solution for part_b"""
    elves = [Elf(_) for _ in parse_input(in_str)]
    dir_names = [get_dir_name(_) for _ in range(4)]
    round_num = 1
    while single_round(elves, dir_names):
        round_num += 1
    return round_num
