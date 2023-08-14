"""tests of adv_2022_01"""

import pytest
import general_utils as gu
import solutions.adv_2022_01 as sol

_DAY_NUM = 1


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_f():
    return gu.read_input(_DAY_NUM, "f")


def _data_b():
    return gu.read_input(_DAY_NUM, "b")


def test_parse_input():
    """tests parse_input agains example data"""
    expected = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    actual = sol.parse_input(_data_small())
    assert expected == actual


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 24000),
        (_data_p(), 69912),
        (_data_f(), 66487),
        (_data_b(), 68923),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 45000),
        (_data_p(), 208180),
        (_data_f(), 197301),
        (_data_b(), 200044),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
