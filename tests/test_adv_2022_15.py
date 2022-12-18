"""tests of adv_2022_15"""

import pytest
import sympy
import general_utils as gu
import solutions.adv_2022_15 as sol

_DAY_NUM = 15


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_data_small())
    expected = [
        sol.SensorReading((2, 18), (-2, 15)),
        sol.SensorReading((9, 16), (10, 16)),
        sol.SensorReading((13, 2), (15, 3)),
        sol.SensorReading((12, 14), (10, 16)),
        sol.SensorReading((10, 20), (10, 16)),
        sol.SensorReading((14, 17), (10, 16)),
        sol.SensorReading((8, 7), (2, 10)),
        sol.SensorReading((2, 0), (2, 10)),
        sol.SensorReading((0, 11), (2, 10)),
        sol.SensorReading((20, 14), (25, 17)),
        sol.SensorReading((17, 20), (21, 22)),
        sol.SensorReading((16, 7), (15, 3)),
        sol.SensorReading((14, 3), (15, 3)),
        sol.SensorReading((20, 1), (15, 3)),
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "input_row,expected",
    [
        (-4, sympy.S.EmptySet),
        (-3, sympy.S.EmptySet),
        (-2, sympy.Interval(8, 8)),
        (-1, sympy.Interval(7, 9)),
        (0, sympy.Interval(6, 10)),
        (1, sympy.Interval(5, 11)),
        (2, sympy.Interval(4, 12)),
        (3, sympy.Interval(3, 13)),
        (4, sympy.Interval(2, 14)),
        (5, sympy.Interval(1, 15)),
        (6, sympy.Interval(0, 16)),
        (7, sympy.Interval(-1, 17)),
        (8, sympy.Interval(0, 16)),
        (9, sympy.Interval(1, 15)),
        (15, sympy.Interval(7, 9)),
        (16, sympy.Interval(8, 8)),
        (17, sympy.S.EmptySet),
        (18, sympy.S.EmptySet),
    ],
)
def test_get_covered_interval(input_row, expected):
    """tests covered_interval"""
    sensor = sol.SensorReading((8, 7), (2, 10))
    assert sensor.get_covered_interval(input_row) == expected


def test_count_safe_in_row():
    """tests count_safe_in_row with example data"""
    assert sol.count_safe_in_row(sol.parse_input(_data_small()), 10) == 26


def test_solve_a():
    """tests solve_a"""
    assert sol.solve_a(_data_p()) == 4827924


def test_find_distress_beacon_fine():
    """tests find_distress_beacon with example data"""
    assert sol.find_distress_beacon_fine(
        sol.parse_input(_data_small()), 0, 20, 0, 20
    ) == (
        14,
        11,
    )


def test_find_distress_beacon():
    """tests find_distress_beacon with example data"""
    assert sol.find_distress_beacon(sol.parse_input(_data_small()), 0, 20, 0, 20) == (
        14,
        11,
    )


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (14, 11, 56000011),
        (10, 2, 40000002),
        (1, 0, 4000000),
    ],
)
def test_tuning_frequency(input_x, input_y, expected):
    """tests tuning_frequency"""
    assert sol.tuning_frequency(input_x, input_y) == expected


def test_solve_b():
    """tests solve_b"""
    assert sol.solve_b(_data_p()) == 12977110973564
