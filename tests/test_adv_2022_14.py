"""tests of adv_2022_14"""

import pytest
import solutions.adv_2022_14 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(14, {"small", "p", "s"})
_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_DATA_SMALL)
    expected = (
        ((498, 4), (498, 6), (496, 6)),
        ((503, 4), (502, 4), (502, 9), (494, 9)),
    )
    assert actual == expected


@pytest.mark.parametrize(
    "input_start,input_end,expected",
    [
        ((10, 5), (15, 5), {(_, 5) for _ in range(10, 16)}),
        ((3, 2), (3, 7), {(3, _) for _ in range(2, 8)}),
    ],
)
def test_add_segment(input_start, input_end, expected):
    """tests add_line"""
    cur_wall = set()
    sol.add_segment(cur_wall, input_start, input_end)
    assert cur_wall == expected


def test_generate_wall():
    """tests generate_wall with example data"""
    actual = sol.generate_wall(sol.parse_input(_DATA_SMALL))
    expected = {
        (494, 9),
        (495, 9),
        (496, 9),
        (497, 9),
        (498, 9),
        (499, 9),
        (500, 9),
        (501, 9),
        (502, 9),
        (502, 8),
        (502, 7),
        (502, 6),
        (502, 5),
        (502, 4),
        (503, 4),
        (496, 6),
        (497, 6),
        (498, 6),
        (498, 5),
        (498, 4),
    }
    assert actual == expected


def test_y_limit():
    """tests y_limit with example data"""
    scene = sol.generate_wall(sol.parse_input(_DATA_SMALL))

    assert sol.y_limit(scene) == 10


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (24, 93),
        "p": (901, 24589),
        "s": (843, 27625),
    },
)
