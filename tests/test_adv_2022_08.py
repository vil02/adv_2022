"""tests of adv_2022_09"""

import pytest
import general_utils as gu
import solutions.adv_2022_08 as sol

_DAY_NUM = 8


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse_input agains example data"""
    actual = sol.parse_input(_data_small())
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
    assert sol.get_height(sol.parse_input(_data_small()), in_pos) == expected


def test_compute_is_visible():
    """tests compute_is_visible agains example height data"""
    actual = sol.compute_is_visible(sol.parse_input(_data_small()))
    expected = [
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, False, True, False, True],
        [True, True, True, True, True],
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 21, id="small"),
        pytest.param(_data_p(), 1829, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


def test_compute_all_scenic_scores():
    """tests compute_all_scenic_scores with example height data"""
    actual = sol.compute_all_scenic_scores(sol.parse_input(_data_small()))
    expected = [
        [0, 0, 0, 0, 0],
        [0, 1, 4, 1, 0],
        [0, 6, 1, 2, 0],
        [0, 1, 8, 3, 0],
        [0, 0, 0, 0, 0],
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 8, id="small"),
        pytest.param(_data_p(), 291840, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
