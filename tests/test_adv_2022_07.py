"""tests of adv_2022_07"""

import collections
import pytest
import solutions.adv_2022_07 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(7, {"small", "small_r", "p", "s", "b", "t"})


_EXAMPLE_DATA = sol.parse_input(_INPUTS.inputs["small"])
assert _EXAMPLE_DATA is not None

Sizes = collections.namedtuple("Sizes", ["simple_size", "total_size"])
_EXPECTED_SIZES = {
    "/|": Sizes(14848514 + 8504156, 48381165),
    "/|a|": Sizes(29116 + 2557 + 62596, 29116 + 2557 + 62596 + 584),
    "/|a|e|": Sizes(584, 584),
    "/|d|": Sizes(
        4060174 + 8033020 + 5626152 + 7214296, 4060174 + 8033020 + 5626152 + 7214296
    ),
}


@pytest.mark.parametrize(
    "dir_path, expected",
    [(dir_path, size.simple_size) for (dir_path, size) in _EXPECTED_SIZES.items()],
)
def test_all_file_size(dir_path, expected):
    """tests Dictionary.all_file_size against example data"""
    assert _EXAMPLE_DATA[dir_path].all_file_size() == expected


@pytest.mark.parametrize(
    "dir_path, expected",
    [(dir_path, size.total_size) for (dir_path, size) in _EXPECTED_SIZES.items()],
)
def test_get_dir_size(dir_path, expected):
    """tests get_dir_size against example data"""
    assert sol.get_dir_size(dir_path, _EXAMPLE_DATA) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (95437, 24933642),
        "small_r": (99999, 50099999),
        "p": (1453349, 2948823),
        "s": (1501149, 10096985),
        "b": (1908462, 3979145),
        "t": (1350966, 6296435),
    },
)
