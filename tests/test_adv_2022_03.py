"""tests of adv_2022_03"""

import pytest
import general_utils as gu
import solutions.adv_2022_03 as sol

_DAY_NUM = 3


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


@pytest.mark.parametrize(
    "input_char,expected",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
        ("a", 1),
        ("z", 26),
        ("A", 27),
        ("Z", 52),
    ],
)
def test_get_priority(input_char, expected):
    """tests get_priority"""
    assert sol.get_priority(input_char) == expected


@pytest.mark.parametrize(
    "input_char",
    ["1", "@", "!", "{", ")", "[", "`"],
)
def test_get_priority_raises_error(input_char):
    """tests get_priority"""
    with pytest.raises(ValueError):
        sol.get_priority(input_char)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 157),
        (_data_p(), 8298),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (_data_small(), 70),
        (_data_p(), 2708),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
