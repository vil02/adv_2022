"""tests of adv_2022_07"""

import pytest
import general_utils as gu
import solutions.adv_2022_07 as sol

_DAY_NUM = 7


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 95437, id="small"),
        pytest.param(
            _data_p(), 1453349, id="p"
        ),  # > 1069240 # < 1482845 nie 1318735 nie 1179500
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 24933642, id="small"),
        pytest.param(_data_p(), 2948823, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
