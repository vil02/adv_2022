"""solution of adv_2022_16"""

import re
import collections

Valve = collections.namedtuple("Valve", ["flow_rate", "targets"])


def _proc_targets_str(in_targets_str):
    return set(in_targets_str.split(", "))


def _check_valves(in_valves):
    assert in_valves["AA"].flow_rate == 0
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
