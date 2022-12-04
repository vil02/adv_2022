"""tests of adv_2022_04"""

import pytest
import general_utils as gu
import solutions.adv_2022_04 as sol

_DAY_NUM = 4


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _add_reversed(in_list):
    res = in_list + [tuple(reversed(_)) for _ in in_list]
    return list(set(res))


@pytest.mark.parametrize(
    "in_a,in_b",
    _add_reversed(
        [
            ((2, 4), (2, 4)),
            ((3, 3), (1, 4)),
            ((3, 4), (2, 5)),
            ((3, 7), (7, 7)),
        ]
    ),
)
def test_is_one_fully_contained_positive(in_a, in_b):
    """positive tests of is_one_fully_contained"""
    assert sol.is_one_fully_contained(in_a, in_b)


@pytest.mark.parametrize(
    "in_a,in_b",
    _add_reversed(
        [
            ((2, 5), (3, 6)),
            ((3, 3), (4, 4)),
        ]
    ),
)
def test_is_one_fully_contained_negative(in_a, in_b):
    """negative tests of is_one_fully_contained"""
    assert not sol.is_one_fully_contained(in_a, in_b)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 2, id="small"),
        pytest.param(_data_p(), 433, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "in_a,in_b",
    _add_reversed(
        [
            ((2, 4), (3, 4)),
            ((3, 3), (2, 4)),
            ((3, 4), (1, 3)),
        ]
    ),
)
def test_do_intersect_positive(in_a, in_b):
    """positive tests of do_intersect"""
    assert sol.do_intersect(in_a, in_b)


@pytest.mark.parametrize(
    "in_a,in_b",
    _add_reversed(
        [
            ((2, 4), (5, 6)),
            ((3, 3), (4, 4)),
            ((1, 2), (3, 4)),
        ]
    ),
)
def test_do_intersect_negative(in_a, in_b):
    """negative tests of do_intersect"""
    assert not sol.do_intersect(in_a, in_b)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 4, id="small"),
        pytest.param(_data_p(), 852, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
