"""solution of adv_2022_16"""

import math
import re
import collections
import functools

Valve = collections.namedtuple("Valve", ["flow_rate", "targets"])


def _proc_targets_str(in_targets_str):
    return set(in_targets_str.split(", "))


_INITIAL_VALVE = "AA"


def _check_valves(in_valves):
    assert in_valves[_INITIAL_VALVE].flow_rate == 0
    for cur_cave in in_valves.values():
        assert all(_ in in_valves for _ in cur_cave.targets)


def _parse_single_valve(in_line):
    match = re.search(
        r"Valve (?P<valve_name>[A-Z]{2}) has flow rate=(?P<flow_rate>\d+);"
        r" tunnels? leads? to valves? (?P<targets>[A-Z]{2}(, [A-Z]{2})*)",
        in_line,
    )
    return match.group("valve_name"), Valve(
        flow_rate=int(match.group("flow_rate")),
        targets=_proc_targets_str(match.group("targets")),
    )


def parse_input(in_str):
    """parses the input into a dictionary"""
    res = dict(_parse_single_valve(_) for _ in in_str.splitlines())
    _check_valves(res)
    return res


def compute_distances(in_valves, in_start_node):
    """
    returns a dict res where res[end] is the distance between in_start_node and end
    """
    unvisited = set(in_valves.keys())
    res = {_: math.inf for _ in unvisited}
    res[in_start_node] = 0

    def _get_next_node():
        return min(unvisited, key=res.get)

    while unvisited:
        cur_node = _get_next_node()
        for _ in in_valves[cur_node].targets:
            if _ in unvisited:
                res[_] = min(res[cur_node] + 1, res[_])
        unvisited.remove(cur_node)
    return res


def compute_all_distances(in_valves):
    """
    returns a dict res, where res[start][end] is the distance between
    start and end
    """
    return {_: compute_distances(in_valves, _) for _ in in_valves.keys()}


def is_nth_bit_set(in_mask, in_bit_num):
    """returns the in_bit_num bit in in_mask"""
    return bool(in_mask & (1 << in_bit_num))


def _get_set_and_mask_related(in_valves):
    valve_to_num = {valve: valve_num for valve_num, valve in enumerate(in_valves)}
    num_to_valve = {valve_num: valve for valve, valve_num in valve_to_num.items()}
    number_of_valves = len(in_valves)

    def _set_to_mask(in_set):
        return sum(2 ** valve_to_num[_] for _ in in_set)

    def _mask_to_set(in_mask):
        return {
            num_to_valve[_]
            for _ in range(number_of_valves)
            if is_nth_bit_set(in_mask, _)
        }

    return _set_to_mask, _mask_to_set


def get_openable_valves(in_valves):
    """returns the valves, with flow_rate > 0"""
    return {
        valve for valve, properties in in_valves.items() if properties.flow_rate > 0
    }


def get_compute_max(in_valves):
    """
    returns the function computing the maximal preasure,
    which can be released in in_time_limit
    """
    dists = compute_all_distances(in_valves)

    set_to_mask, mask_to_set = _get_set_and_mask_related(get_openable_valves(in_valves))

    @functools.lru_cache(maxsize=None)
    def _inner(cur_valve, cur_opened_mask, cur_time_left):
        assert cur_time_left >= 0
        cur_opened = mask_to_set(cur_opened_mask)
        cur_max = 0
        for new_valve, distance in dists[cur_valve].items():
            new_time_left = cur_time_left - (distance + 1)
            if (
                new_time_left >= 0
                and in_valves[new_valve].flow_rate > 0
                and new_valve not in cur_opened
            ):
                cur_max = max(
                    cur_max,
                    in_valves[new_valve].flow_rate * new_time_left
                    + _inner(
                        new_valve,
                        set_to_mask(cur_opened.union({new_valve})),
                        new_time_left,
                    ),
                )

        return cur_max

    return _inner, set_to_mask


def solve_a(in_str):
    """returns the solution for part_a"""
    compute_max, set_to_mask = get_compute_max(parse_input(in_str))
    return compute_max(_INITIAL_VALVE, set_to_mask(set()), 30)


def _invert_mask(in_mask, in_number_of_valves):
    return sum(
        2**_ for _ in range(in_number_of_valves) if not is_nth_bit_set(in_mask, _)
    )


def _gen_all_mask_pairs(in_number_of_valves):
    for _ in range(1 << (in_number_of_valves - 1)):
        yield _, _invert_mask(_, in_number_of_valves)


def solve_b(in_str):
    """returns the solution for part_b"""
    valves = parse_input(in_str)

    compute_max_fun, _ = get_compute_max(valves)
    res = 0
    for mask_a, mask_b in _gen_all_mask_pairs(len(get_openable_valves(valves))):
        res = max(
            res,
            compute_max_fun(_INITIAL_VALVE, mask_a, 26)
            + compute_max_fun(_INITIAL_VALVE, mask_b, 26),
        )
    return res
