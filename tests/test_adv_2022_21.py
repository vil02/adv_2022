"""tests of adv_2022_00"""

import pytest
import general_utils as gu
import solutions.adv_2022_21 as sol

_DAY_NUM = 21


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse_input with example data"""
    expected = {
        "root": sol.Operation(operation="+", register_a="pppw", register_b="sjmn"),
        "dbpl": 5,
        "cczh": sol.Operation(operation="+", register_a="sllz", register_b="lgvd"),
        "zczc": 2,
        "ptdq": sol.Operation(operation="-", register_a="humn", register_b="dvpt"),
        "dvpt": 3,
        "lfqf": 4,
        "humn": 5,
        "ljgn": 2,
        "sjmn": sol.Operation(operation="*", register_a="drzm", register_b="dbpl"),
        "sllz": 4,
        "pppw": sol.Operation(operation="/", register_a="cczh", register_b="lfqf"),
        "lgvd": sol.Operation(operation="*", register_a="ljgn", register_b="ptdq"),
        "drzm": sol.Operation(operation="-", register_a="hmdt", register_b="zczc"),
        "hmdt": 32,
    }
    assert sol.parse_input(_data_small()) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 152, id="small"),
        pytest.param(_data_p(), 331319379445180, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 301, id="small"),
        pytest.param(_data_p(), 3715799488132, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
