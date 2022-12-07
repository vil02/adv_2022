"""tests of adv_2022_02"""

import pytest
import general_utils as gu
import solutions.adv_2022_02 as sol

_DAY_NUM = 2


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 15),
        (_data_p(), 10941),
        (_data_s(), 11666),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 12),
        (_data_p(), 13071),
        (_data_s(), 12767),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
