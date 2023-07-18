"""tests of adv_2022_14"""

import pytest
import general_utils as gu
import solutions.adv_2022_14 as sol

_DAY_NUM = 14


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_data_small())
    expected = (
        ((498, 4), (498, 6), (496, 6)),
        ((503, 4), (502, 4), (502, 9), (494, 9)),
    )
    assert actual == expected


@pytest.mark.parametrize(
    "input_start,input_end,expected",
    [
        ((10, 5), (15, 5), {(_, 5) for _ in range(10, 16)}),
        ((3, 2), (3, 7), {(3, _) for _ in range(2, 8)}),
    ],
)
def test_add_segment(input_start, input_end, expected):
    """tests add_line"""
    cur_wall = set()
    sol.add_segment(cur_wall, input_start, input_end)
    assert cur_wall == expected


def test_generate_wall():
    """tests generate_wall with example data"""
    actual = sol.generate_wall(sol.parse_input(_data_small()))
    expected = {
        (494, 9),
        (495, 9),
        (496, 9),
        (497, 9),
        (498, 9),
        (499, 9),
        (500, 9),
        (501, 9),
        (502, 9),
        (502, 8),
        (502, 7),
        (502, 6),
        (502, 5),
        (502, 4),
        (503, 4),
        (496, 6),
        (497, 6),
        (498, 6),
        (498, 5),
        (498, 4),
    }
    assert actual == expected


def test_y_limit():
    """tests y_limit with example data"""
    scene = sol.generate_wall(sol.parse_input(_data_small()))

    assert sol.y_limit(scene) == 10


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 24, id="small"),
        pytest.param(_data_p(), 901, id="p"),
        pytest.param(_data_s(), 843, id="s"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 93, id="small"),
        pytest.param(_data_p(), 24589, id="p"),
        pytest.param(_data_s(), 27625, id="s"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
