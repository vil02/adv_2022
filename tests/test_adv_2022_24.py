"""tests of adv_2022_00"""

import pytest
import general_utils as gu
import solutions.adv_2022_24 as sol

_DAY_NUM = 24


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "input_size, input_pos, expected",
    [
        ((10, 10), (0, 0), {(0, 0), (0, -1), (0, 1), (1, 0)}),
        ((10, 10), (1, 1), {(1, 1), (1, 0), (1, 2), (0, 1), (2, 1)}),
        ((10, 10), (0, -1), {(0, -1), (0, 0)}),
        ((10, 10), (9, 9), {(9, 9), (9, 10), (8, 9), (9, 8)}),
    ],
)
def test_position_candidates(input_size, input_pos, expected):
    """tests position_candidates"""
    assert set(sol.position_candidates(input_size, input_pos)) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 18, id="small"),
        pytest.param(_data_p(), 221, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 54, id="small"),
        pytest.param(_data_p(), 739, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
