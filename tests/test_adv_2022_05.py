"""tests of adv_2022_05"""

import pytest
import general_utils as gu
import solutions.adv_2022_05 as sol

_DAY_NUM = 5


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "input_col,expected",
    [
        (1, 1),
        (5, 2),
        (9, 3),
    ],
)
def test_get_stack_number(input_col, expected):
    """tests get_stack_number"""
    assert sol.get_stack_number(input_col) == expected


def test_parse_input():
    """tests parse_input"""
    actual_state, actual_moves = sol.parse_input(_data_small())
    expected_state = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}
    expected_moves = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
    assert actual_state == expected_state
    assert actual_moves == expected_moves


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), "CMZ", id="small"),
        pytest.param(_data_p(), "LJSVLTWQM", id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), "MCD", id="small"),
        pytest.param(_data_p(), "BRQWDBBJM", id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
