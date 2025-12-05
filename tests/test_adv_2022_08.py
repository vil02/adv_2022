"""tests of adv_2022_08"""

import pytest
import solutions.adv_2022_08 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(8, {"small", "p", "s", "b", "t"})

_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input against example data"""
    actual = sol.parse_input(_DATA_SMALL)
    expected = (
        (3, 0, 3, 7, 3),
        (2, 5, 5, 1, 2),
        (6, 5, 3, 3, 2),
        (3, 3, 5, 4, 9),
        (3, 5, 3, 9, 0),
    )
    assert actual == expected


@pytest.mark.parametrize(
    "in_pos,expected",
    [
        ((-1, 0), -1),
        ((0, -1), -1),
        ((0, 0), 3),
        ((3, 0), 7),
        ((3, 1), 1),
        ((4, 1), 2),
        ((5, 1), -1),
        ((2, 4), 3),
        ((2, 5), -1),
    ],
)
def test_get_height(in_pos, expected):
    """tests get_height with example height data"""
    assert sol.get_height(sol.parse_input(_DATA_SMALL), in_pos) == expected


def test_compute_is_visible():
    """tests compute_is_visible against example height data"""
    actual = sol.compute_is_visible(sol.parse_input(_DATA_SMALL))
    expected = [
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, False, True, False, True],
        [True, True, True, True, True],
    ]
    assert actual == expected


def test_compute_all_scenic_scores():
    """tests compute_all_scenic_scores with example height data"""
    actual = sol.compute_all_scenic_scores(sol.parse_input(_DATA_SMALL))
    expected = [
        [0, 0, 0, 0, 0],
        [0, 1, 4, 1, 0],
        [0, 6, 1, 2, 0],
        [0, 1, 8, 3, 0],
        [0, 0, 0, 0, 0],
    ]
    assert actual == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (21, 8),
        "p": (1829, 291840),
        "s": (1814, 330786),
        "b": (1854, 527340),
    },
)
