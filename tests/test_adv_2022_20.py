"""tests of adv_2022_00"""

import pytest
import solutions.adv_2022_20 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(20, {"small", "p"})


_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input"""
    assert sol.parse_input(_DATA_SMALL) == (1, 2, -3, 3, -2, 0, 4)


@pytest.mark.parametrize(
    "input_index,expected",
    [
        (1000, 4),
        (2000, -3),
        (3000, 2),
        (0, 0),
        (-1, 4),
        (-2, -3),
        (-3, 2),
        (-4, 1),
        (-5, -2),
        (-6, 3),
        (-7, 0),
        (-8, 4),
        (1, 3),
        (2, -2),
        (3, 1),
        (4, 2),
        (5, -3),
        (6, 4),
        (7, 0),
        (8, 3),
    ],
)
def test_get_nth_after_zero(input_index, expected):
    """tests get_nth_after_zero"""
    example_list = (1, 2, -3, 4, 0, 3, -2)
    assert sol.get_nth_after_zero(example_list, input_index) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        ((0, 1, 2), ((0, 0), (1, 0), (2, 0))),
        ((0, 1, 1), ((0, 0), (1, 0), (1, 1))),
        ((1, 1, 1), ((1, 0), (1, 1), (1, 2))),
        ((1, 2, 1, 2, 1, 3), ((1, 0), (2, 0), (1, 1), (2, 1), (1, 2), (3, 0))),
    ],
)
def test_mark_duplicates(input_data, expected):
    """tests mark_duplicates"""
    assert sol.mark_duplicates(input_data) == expected


@pytest.mark.parametrize(
    "input_tuple,input_num,expected",
    [
        ((1, 2, -3, 3, -2, 0, 4), 1, (2, 1, -3, 3, -2, 0, 4)),
        ((2, 1, -3, 3, -2, 0, 4), 2, (1, -3, 2, 3, -2, 0, 4)),
        ((1, -3, 2, 3, -2, 0, 4), -3, (1, 2, 3, -2, -3, 0, 4)),
        ((1, 2, 3, -2, -3, 0, 4), 3, (1, 2, -2, -3, 0, 3, 4)),
        ((1, 2, -2, -3, 0, 3, 4), -2, (-2, 1, 2, -3, 0, 3, 4)),
        ((1, 2, -3, 0, 3, 4, -2), 0, (1, 2, -3, 0, 3, 4, -2)),
        ((1, 2, -3, 0, 3, 4, -2), 4, (1, 2, -3, 4, 0, 3, -2)),
        ((-2, 1, 2, -3, 0, 3, 4), 4, (-2, 1, 2, -3, 4, 0, 3)),
        ((4, 5, 6, 1, 7, 8, 9), 1, (4, 5, 6, 7, 1, 8, 9)),
        ((4, -2, 5, 6, 7, 8, 9), -2, (4, 5, 6, 7, 8, -2, 9)),
        ((10, 20, 30, 1), 1, (10, 1, 20, 30)),
        ((10, 20, 30, 2), 2, (10, 20, 2, 30)),
        ((10, 20, 30, 3), 3, (3, 10, 20, 30)),
        ((10, 20, 30, 4), 4, (10, 4, 20, 30)),
        ((10, 20, 30, 5), 5, (10, 20, 5, 30)),
        ((10, 20, 30, 6), 6, (6, 10, 20, 30)),
        ((10, 20, 30, 7), 7, (10, 7, 20, 30)),
        ((10, 20, 30, 8), 8, (10, 20, 8, 30)),
        ((10, 20, 30, -1), -1, (10, 20, -1, 30)),
        ((10, 20, 30, -2), -2, (10, -2, 20, 30)),
        ((10, 20, 30, -3), -3, (-3, 10, 20, 30)),
        ((10, 20, 30, -4), -4, (10, 20, -4, 30)),
        ((10, 20, 30, -5), -5, (10, -5, 20, 30)),
        ((10, 20, 30, -6), -6, (-6, 10, 20, 30)),
        ((10, 20, 30, -7), -7, (10, 20, -7, 30)),
        ((-1, 10, 20, 30), -1, (10, 20, -1, 30)),
        ((-2, 10, 20, 30), -2, (10, -2, 20, 30)),
    ],
)
def test_make_mix(input_tuple, input_num, expected):
    """tests make_mix with example data"""
    assert len(set(input_tuple)) == len(input_tuple)
    tmp_list = list(sol.mark_duplicates(input_tuple))
    sol.make_mix(tmp_list, (input_num, 0))
    assert tuple(tmp_list) == sol.mark_duplicates(expected)


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (3, 1623178306),
        "p": (872, 5382459262696),
    },
)
