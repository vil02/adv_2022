"""solution of adv_2022_19"""

import re
import collections

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
