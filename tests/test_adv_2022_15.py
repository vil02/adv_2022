"""tests of adv_2022_15"""

import pytest
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
        (-4, None),
        (-3, None),
        (-2, (8, 8)),
        (-1, (7, 9)),
        (0, (6, 10)),
        (1, (5, 11)),
        (2, (4, 12)),
        (3, (3, 13)),
        (4, (2, 14)),
        (5, (1, 15)),
        (6, (0, 16)),
        (7, (-1, 17)),
        (8, (0, 16)),
        (9, (1, 15)),
        (15, (7, 9)),
        (16, (8, 8)),
        (17, None),
        (18, None),
    ],
)
def test_get_covered_interval(input_row, expected):
    sensor = sol.SensorReading((8, 7), (2, 10))
    assert sensor.get_covered_interval(input_row) == expected


def test_count_safe_in_row():
    assert sol.count_safe_in_row(sol.parse_input(_data_small()), 10) == 26


def test_solve_a():
    assert sol.solve_a(_data_p()) == 4827924


# @pytest.mark.parametrize(
#     "input_str,expected",
#     [
#         pytest.param(_data_small(), 10, id="small"),
#         pytest.param(_data_p(), 11, id="p"),
#     ],
# )
# def test_solve_a(input_str, expected):
#     """tests solve_a"""
#     assert sol.solve_a(input_str) == expected
#
#
# @pytest.mark.parametrize(
#     "input_str,expected",
#     [
#         pytest.param(_data_small(), 20, id="small"),
#         pytest.param(_data_p(), 22, id="p"),
#     ],
# )
# def test_solve_b(input_str, expected):
#     """tests solve_b"""
#     assert sol.solve_b(input_str) == expected
