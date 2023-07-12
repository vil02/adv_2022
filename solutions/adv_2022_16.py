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


def compute_max(in_valves, in_time_limit):
    """
    computes the maximal preasure, which can be released in in_time_limit
    """
    dists = compute_all_distances(in_valves)

    @functools.lru_cache(maxsize=None)
    def _inner(cur_valve, cur_opened, cur_time_left):
        assert cur_time_left >= 0
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
                        cur_opened.union({new_valve}),
                        new_time_left,
                    ),
                )
        return cur_max

    return _inner(_INITIAL_VALVE, frozenset(), in_time_limit)


def solve_a(in_str):
    """returns the solution for part_a"""
    return compute_max(parse_input(in_str), 30)
