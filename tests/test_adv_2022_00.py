"""
tests of adv_2022_00
"""

import pytest
import general_utils as gu
import solutions.adv_2022_00 as sol

_DAY_NUM = 0


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize("input_str,expected", [(_data_p(), 7)])
def test_solve_a(input_str, expected):
    """
    tests solve_a
    """
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [(_data_p(), 7)])
def test_solve_b(input_str, expected):
    """
    tests solve_b
    """
    assert sol.solve_b(input_str) == expected
