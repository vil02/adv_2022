"""solution of adv_2022_18"""

import collections
import math


def parse_input(in_str):
    """parses the input into a tuple of tuples"""

    def _proc_single_line(in_line):
        res = tuple(int(_) for _ in in_line.split(","))
        assert len(res) == 3
        return res

    return tuple(_proc_single_line(_) for _ in in_str.splitlines())


def _shift_pos(in_pos, in_shift):
    return tuple(a + b for a, b in zip(in_pos, in_shift))


def _get_walls(in_pos):
    def _shift_cube_pos(in_shift):
        return _shift_pos(in_pos, in_shift)

    vert_0 = in_pos
    vert_1 = _shift_cube_pos((1, 0, 0))
    vert_2 = _shift_cube_pos((1, 1, 0))
    vert_3 = _shift_cube_pos((0, 1, 0))

    vert_4 = _shift_cube_pos((0, 0, 1))
    vert_5 = _shift_cube_pos((1, 0, 1))
    vert_6 = _shift_cube_pos((1, 1, 1))
    vert_7 = _shift_cube_pos((0, 1, 1))
    assert len({vert_0, vert_1, vert_2, vert_3, vert_4, vert_5, vert_6, vert_7}) == 8
    return frozenset(
        [
            frozenset([vert_0, vert_1, vert_2, vert_3]),
            frozenset([vert_4, vert_5, vert_6, vert_7]),
            frozenset([vert_0, vert_1, vert_5, vert_4]),
            frozenset([vert_3, vert_2, vert_6, vert_7]),
            frozenset([vert_0, vert_3, vert_7, vert_4]),
            frozenset([vert_1, vert_2, vert_6, vert_5]),
        ]
    )


def _calculate_area(in_cubes):
    walls = set()
    removed_walls = set()
    for _ in in_cubes:
        for cur_wall in _get_walls(_):
            if cur_wall not in walls and cur_wall not in removed_walls:
                walls.add(cur_wall)
            else:
                walls.remove(cur_wall)
                removed_walls.add(cur_wall)
    return len(walls)


def solve_a(in_str):
    """returns the solution for part_a"""
    return _calculate_area(parse_input(in_str))


def _update_bound(in_fun, in_bound, in_pos):
    return tuple(in_fun(b, p) for b, p in zip(in_bound, in_pos))


def _calculate_bounds(in_cubes):
    mins = (math.inf, math.inf, math.inf)
    maxs = (-math.inf, -math.inf, -math.inf)
    for _ in in_cubes:
        mins = _update_bound(min, mins, _)
        maxs = _update_bound(max, maxs, _)
    mins = tuple(_ - 1 for _ in mins)
    maxs = tuple(_ + 1 for _ in maxs)

    return collections.namedtuple("Bounds", ["mins", "maxs"])(mins, maxs)


def _is_in_bounds(bounds, in_pos):
    return all(low <= p <= up for low, p, up in zip(bounds.mins, in_pos, bounds.maxs))


def _fill_outer(in_cubes, bounds):
    active = [bounds.mins]
    res = set()
    while active:
        cur_pos = active.pop(0)
        if (
            _is_in_bounds(bounds, cur_pos)
            and cur_pos not in res
            and cur_pos not in in_cubes
        ):
            res.add(cur_pos)
            for _ in [
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1),
            ]:
                active.append(_shift_pos(cur_pos, _))
    return res


def _box_area(bounds):
    d_x, d_y, d_z = (1 + up - low for low, up in zip(bounds.mins, bounds.maxs))
    return 2 * (d_x * d_y + d_y * d_z + d_z * d_x)


def solve_b(in_str):
    """returns the solution for part_b"""
    cubes = frozenset(parse_input(in_str))

    bounds = _calculate_bounds(cubes)
    outer_cubes = _fill_outer(cubes, bounds)
    outer_cubes_total_area = _calculate_area(outer_cubes)
    outer_cubes_outer_area = _box_area(bounds)
    return outer_cubes_total_area - outer_cubes_outer_area
