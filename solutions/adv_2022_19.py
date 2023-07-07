"""solution of adv_2022_19"""

import re
import collections
import math
import functools

Blueprint = collections.namedtuple(
    "Blueprint",
    [
        "id",
        "robot_costs",
    ],
)


def parse_blueprint(in_str):
    """parses the single line of the input into a Blueprint object"""
    match = re.search(
        r"Blueprint (?P<id>\d+): "
        r"Each ore robot costs (?P<ore_robot_ore>\d+) ore. "
        r"Each clay robot costs (?P<clay_robot_ore>\d+) ore. "
        r"Each obsidian robot costs (?P<obsidian_robot_ore>\d+) ore "
        r"and (?P<obsidian_robot_clay>\d+) clay. "
        r"Each geode robot costs (?P<geode_robot_ore>\d+) ore "
        r"and (?P<geode_robot_obsidian>\d+) obsidian.",
        in_str,
    )

    def _as_int(in_name):
        return int(match.group(in_name))

    return Blueprint(
        id=_as_int("id"),
        robot_costs={
            "ore": {"ore": _as_int("ore_robot_ore")},
            "clay": {"ore": _as_int("clay_robot_ore")},
            "obsidian": {
                "ore": _as_int("obsidian_robot_ore"),
                "clay": _as_int("obsidian_robot_clay"),
            },
            "geode": {
                "ore": _as_int("geode_robot_ore"),
                "obsidian": _as_int("geode_robot_obsidian"),
            },
        },
    )


def parse_input(in_str):
    """parses the input into a tuple of Blueprints"""
    return tuple(parse_blueprint(_) for _ in in_str.splitlines())


def compute_quality_level(in_id, in_maximal_number_of_genodes):
    """computes quality level for given ID and number of genodes"""
    assert in_id > 0
    return in_id * in_maximal_number_of_genodes


_NAMES = ("ore", "clay", "obsidian", "geode")


def blueprint_to_raw_format_single(in_cost_dict):
    """
    converts a dictorinary representing costs of building single robot into a tuple
    """
    pos_dict = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
    res = [0 for _ in range(len(pos_dict))]
    for name, cost in in_cost_dict.items():
        res[pos_dict[name]] = cost
    return tuple(res)


def blueprint_to_raw_format(in_blueprint):
    """converts a Blueprint object into tuples"""
    return tuple(
        blueprint_to_raw_format_single(in_blueprint.robot_costs[_]) for _ in _NAMES
    )


def _can_build(in_resources, in_costs):
    return all(r >= c for r, c in zip(in_resources, in_costs))


def _remove_rerources(in_resources, in_costs):
    return tuple(r - c for r, c in zip(in_resources, in_costs))


def _add_robot(in_robots, in_robot_pos):
    res = list(in_robots)
    res[in_robot_pos] += 1
    return tuple(res)


def _build_robot_and_add_resources(in_resources, in_robots, in_robot_pos, in_costs):
    res_resources = _add_resources(_remove_rerources(in_resources, in_costs), in_robots)
    res_robots = _add_robot(in_robots, in_robot_pos)
    return res_resources, res_robots


def _add_resources(in_resources, in_robots):
    return tuple(r + p for r, p in zip(in_resources, in_robots))


def _to_state(in_resources, in_robots, _time_left):
    return in_resources, in_robots, _time_left


def _get_genode(in_resources):
    return in_resources[-1]


def get_bounds(in_raw_blueprint):
    """
    returns a tuple with maximal costs for each resourse
    """
    res = [
        max(cur_robot_cost[_] for cur_robot_cost in in_raw_blueprint)
        for _ in range(len(_NAMES))
    ]
    assert res[-1] == 0
    res[-1] = math.inf
    return tuple(res)


def _get_initial_state(in_time_limit):
    return _to_state(
        tuple(0 for _ in _NAMES), tuple([1] + [0 for _ in _NAMES[1:]]), in_time_limit
    )


def _to_key(in_resources, in_robots, in_time_left):
    return tuple([in_resources, in_robots, in_time_left])


def _is_too_many_robots(in_robots, in_bounds):
    """
    it does not make sense to have more robots of given type
    than maximal spend rate of given resource
    """
    return any(
        amout_of_robots > bound for amout_of_robots, bound in zip(in_robots, in_bounds)
    )


def _reduce_resources(in_resources, in_time_left, in_bounds):
    """it does not make sense to have more resporces than possible to spend"""
    res = list(in_resources)
    for res_num, bound in enumerate(in_bounds):
        res[res_num] = min(res[res_num], in_time_left * bound)
    return tuple(res)


@functools.lru_cache(maxsize=None)
def evaluate_blueprint(in_raw_blueprint, time_limit):
    """
    returns the maximal amout geodes which can be produced using given
    blueprint in given time
    """
    bounds = get_bounds(in_raw_blueprint)
    max_val = -math.inf
    active = [_get_initial_state(time_limit)]
    known_states = set()

    while active:
        cur_resources, cur_robots, cur_time_left = active.pop()

        if cur_time_left <= 1:
            max_val = max(
                max_val,
                _get_genode(cur_resources) + cur_time_left * _get_genode(cur_robots),
            )
            continue

        if _is_too_many_robots(cur_robots, bounds):
            continue

        cur_resources = _reduce_resources(cur_resources, cur_time_left, bounds)

        if _to_key(cur_resources, cur_robots, cur_time_left) in known_states:
            continue

        new_states = []
        new_states.append(
            tuple([_add_resources(cur_resources, cur_robots), cur_robots])
        )
        for robot_pos, robot_cost in enumerate(in_raw_blueprint):
            if _can_build(cur_resources, robot_cost):
                new_states.append(
                    _build_robot_and_add_resources(
                        cur_resources, cur_robots, robot_pos, robot_cost
                    )
                )

        for _ in new_states:
            active.append(_to_state(*_, cur_time_left - 1))
        known_states.add(_to_key(cur_resources, cur_robots, cur_time_left))
    return max_val


def solve_a(in_str):
    """returns the solution for part_a"""
    blueprints = parse_input(in_str)
    results = {
        _.id: evaluate_blueprint(blueprint_to_raw_format(_), 24) for _ in blueprints
    }
    return sum(compute_quality_level(id, max_val) for id, max_val in results.items())
