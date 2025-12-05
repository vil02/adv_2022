"""tests of adv_2022_03"""

import pytest
import solutions.adv_2022_03 as sol
from . import test_utils as tu


@pytest.mark.parametrize(
    "input_char,expected",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
        ("a", 1),
        ("z", 26),
        ("A", 27),
        ("Z", 52),
    ],
)
def test_get_priority(input_char, expected):
    """tests get_priority"""
    assert sol.get_priority(input_char) == expected


@pytest.mark.parametrize(
    "input_char",
    ["1", "@", "!", "{", ")", "[", "`"],
)
def test_get_priority_raises_error(input_char):
    """tests get_priority"""
    with pytest.raises(ValueError):
        sol.get_priority(input_char)


_INPUTS = tu.get_inputs(3, {"small", "p", "s", "b", "t"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (157, 70),
        "p": (8298, 2708),
        "s": (8109, 2738),
        "b": (7691, 2508),
        "t": (7763, 2569),
    },
)
