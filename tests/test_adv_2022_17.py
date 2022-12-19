"""tests of adv_2022_17"""

import pytest
import general_utils as gu
import solutions.adv_2022_17 as sol

_DAY_NUM = 17


def _data_blocks():
    return gu.read_input(_DAY_NUM, "blocks")


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_blocks():
    """tests parse_blocks"""
    expected = (
        frozenset({(0, 0), (1, 0), (2, 0), (3, 0)}),
        frozenset({(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)}),
        frozenset({(2, 1), (0, 0), (2, 0), (2, 2), (1, 0)}),
        frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
        frozenset({(0, 0), (1, 0), (0, 1), (1, 1)}),
    )
    assert sol.parse_blocks(_data_blocks()) == expected


def test_parse_input():
    """tests parse input with example data"""
    expected = (
        ">",
        ">",
        ">",
        "<",
        "<",
        ">",
        "<",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        "<",
        ">",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        "<",
        ">",
        ">",
        "<",
        "<",
        ">",
        ">",
    )
    assert sol.parse_input(_data_small()) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 3068, id="small"),
        pytest.param(_data_p(), 3181, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 1514285714288, id="small"),
        pytest.param(_data_p(), 1570434782634, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
