"""tests of adv_2022_12"""

import pytest
import general_utils as gu
import solutions.adv_2022_12 as sol

_DAY_NUM = 12


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_data_small())
    assert actual.start_pos == (0, 0)
    assert actual.end_pos == (5, 2)
    assert actual.height_data == _EXAMPLE_HEIGHT_DATA


_EXAMPLE_HEIGHT_DATA = (
    (97, 97, 98, 113, 112, 111, 110, 109),
    (97, 98, 99, 114, 121, 120, 120, 108),
    (97, 99, 99, 115, 122, 122, 120, 107),
    (97, 99, 99, 116, 117, 118, 119, 106),
    (97, 98, 100, 101, 102, 103, 104, 105),
)


@pytest.mark.parametrize(
    "input_pos,expected",
    [
        ((0, 0), ord("a")),
        ((5, 2), ord("z")),
        ((3, 0), ord("q")),
        ((1, 3), ord("c")),
    ],
)
def test_get_height(input_pos, expected):
    """test get_height with _EXAMPLE_HEIGHT_DATA"""
    assert sol.get_height(_EXAMPLE_HEIGHT_DATA, input_pos) == expected


@pytest.mark.parametrize(
    "input_pos,expected",
    [
        ((0, 0), {(0, 1), (1, 0)}),
        ((3, 1), {(3, 0), (3, 2), (2, 1)}),
        ((1, 1), {(0, 1), (2, 1), (1, 0), (1, 2)}),
    ],
)
def test_gen_candidates_a(input_pos, expected):
    """test gen_candidates_a with _EXAMPLE_HEIGHT_DATA"""
    assert set(sol.gen_candidates_a(_EXAMPLE_HEIGHT_DATA, input_pos)) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 31, id="small"),
        pytest.param(_data_p(), 383, id="p"),
        pytest.param(_data_s(), 484, id="s"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 29, id="small"),
        pytest.param(_data_p(), 377, id="p"),
        pytest.param(_data_s(), 478, id="s"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
