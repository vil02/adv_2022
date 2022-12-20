"""tests of adv_2022_18"""

import pytest
import general_utils as gu
import solutions.adv_2022_18 as sol

_DAY_NUM = 18


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_my_1():
    return gu.read_input(_DAY_NUM, "my_1")


def _data_my_2():
    return gu.read_input(_DAY_NUM, "my_2")


def _data_my_3():
    return gu.read_input(_DAY_NUM, "my_3")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse_input with example data"""
    expected = (
        (2, 2, 2),
        (1, 2, 2),
        (3, 2, 2),
        (2, 1, 2),
        (2, 3, 2),
        (2, 2, 1),
        (2, 2, 3),
        (2, 2, 4),
        (2, 2, 6),
        (1, 2, 5),
        (3, 2, 5),
        (2, 1, 5),
        (2, 3, 5),
    )
    assert sol.parse_input(_data_small()) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 64, id="small"),
        pytest.param(_data_my_1(), 6 * 3 * 3 + 6, id="my_1"),
        pytest.param(_data_my_2(), 2 * 9 + 4 * 3 * 4 + 10, id="my_2"),
        pytest.param(_data_my_3(), 2 * 9 + 4 * 3 * 5 + 2 * 6, id="my_3"),
        pytest.param(_data_p(), 4348, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_my_1(), 6 * 3 * 3, id="my_1"),
        pytest.param(_data_my_2(), 2 * 9 + 4 * 3 * 4, id="my_2"),
        pytest.param(_data_my_3(), 2 * 9 + 4 * 3 * 5, id="my_3"),
        pytest.param(_data_small(), 58, id="small"),
        pytest.param(_data_p(), 2546, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
