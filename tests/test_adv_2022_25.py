"""tests of adv_2022_25"""

import pytest
import collections
import general_utils as gu
import solutions.adv_2022_25 as sol

_DAY_NUM = 25


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


SNAFUDecimal = collections.namedtuple("SNAFUDecimal", ["snafu", "decimal"])

_EXAMPLE_SNAFU_DECIMAL = [
    SNAFUDecimal("1=-0-2", 1747),
    SNAFUDecimal("12111", 906),
    SNAFUDecimal("2=0=", 198),
    SNAFUDecimal("21", 11),
    SNAFUDecimal("2=01", 201),
    SNAFUDecimal("111", 31),
    SNAFUDecimal("20012", 1257),
    SNAFUDecimal("112", 32),
    SNAFUDecimal("1=-1=", 353),
    SNAFUDecimal("1-12", 107),
    SNAFUDecimal("12", 7),
    SNAFUDecimal("1=", 3),
    SNAFUDecimal("122", 37),
    SNAFUDecimal("2=-1=0", 4890),
    SNAFUDecimal("1", 1),
    SNAFUDecimal("2", 2),
    SNAFUDecimal("1=", 3),
    SNAFUDecimal("1-", 4),
    SNAFUDecimal("10", 5),
    SNAFUDecimal("11", 6),
    SNAFUDecimal("12", 7),
    SNAFUDecimal("2=", 8),
    SNAFUDecimal("2-", 9),
    SNAFUDecimal("20", 10),
    SNAFUDecimal("1=0", 15),
    SNAFUDecimal("1-0", 20),
    SNAFUDecimal("1=11-2", 2022),
    SNAFUDecimal("1-0---0", 12345),
    SNAFUDecimal("1121-1110-1=0", 314159265),
]


@pytest.mark.parametrize("input_data", _EXAMPLE_SNAFU_DECIMAL)
def test_snafu_to_decimal(input_data):
    """tests solve_a"""
    assert sol.snafu_to_decimal(input_data.snafu) == input_data.decimal


@pytest.mark.parametrize("input_data", _EXAMPLE_SNAFU_DECIMAL)
def test_decimal_to_snafu(input_data):
    """tests solve_a"""
    assert sol.decimal_to_snafu(input_data.decimal) == input_data.snafu


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), "2=-1=0", id="small"),
        pytest.param(_data_p(), "2--2-0=--0--100-=210", id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected
