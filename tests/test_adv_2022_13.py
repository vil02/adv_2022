"""tests of adv_2022_13"""

import pytest
import general_utils as gu
import solutions.adv_2022_13 as sol

_DAY_NUM = 13


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("1,1,3,1,1", ["1", "1", "3", "1", "1"]),
        ("1,[1,3],1,1", ["1", "[1,3]", "1", "1"]),
        ("1,[[1,3],1,1]", ["1", "[[1,3],1,1]"]),
        ("", [""]),
        ("[]", ["[]"]),
        ("[[]]", ["[[]]"]),
        ("[[],[]]", ["[[],[]]"]),
    ],
)
def test_split_lists(input_str, expected):
    """tests split_lists"""
    assert sol.split_lists(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("[1,1,3,1,1]", [1, 1, 3, 1, 1]),
        ("[1,1,5,1,1]", [1, 1, 5, 1, 1]),
        ("[[1],[2,3,4]]", [[1], [2, 3, 4]]),
        ("[[1],4]", [[1], 4]),
        ("[9]", [9]),
        ("[[8,7,6]]", [[8, 7, 6]]),
        ("[[4,4],4,4]", [[4, 4], 4, 4]),
        ("[[4,4],4,4,4]", [[4, 4], 4, 4, 4]),
        ("[7,7,7,7]", [7, 7, 7, 7]),
        ("[7,7,7]", [7, 7, 7]),
        ("[]", []),
        ("[3]", [3]),
        ("[[[]]]", [[[]]]),
        ("[[]]", [[]]),
        ("[1,[2,[3,[4,[5,6,7]]]],8,9]", [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]),
        ("[1,[2,[3,[4,[5,6,0]]]],8,9]", [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    ],
)
def test_parse_list(input_str, expected):
    """tests parse_list"""
    assert sol.parse_list(input_str) == expected


def test_parse_input():
    """tests parse input with example data"""
    actual = sol.parse_input(_data_small())
    expected = (
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        ([[1], [2, 3, 4]], [[1], 4]),
        ([9], [[8, 7, 6]]),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        ([7, 7, 7, 7], [7, 7, 7]),
        ([], [3]),
        ([[[]]], [[]]),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    )
    assert actual == expected


@pytest.mark.parametrize(
    "in_left,in_right",
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        ([[1], [2, 3, 4]], [[1], 4]),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        ([7, 7, 7], [7, 7, 7, 7]),
        ([], [3]),
        ([[6, 8]], [[9, 9, [[9, 8, 4], [6, 1, 1, 7], 8]]]),
        ([[]], [[], [[10, [], [10, 8, 1], [0]]], [1], [[]], [[[4], [7, 2]]]]),
    ],
)
def test_is_in_order_positive(in_left, in_right):
    """tests is_in_order with input for which the result should be 1"""
    assert sol.is_in_order(in_left, in_right) == 1


@pytest.mark.parametrize(
    "in_left,in_right",
    [
        ([1, 1, 5, 1, 1], [1, 1, 3, 1, 1]),
        ([9], [[8, 7, 6]]),
        ([7, 7, 7, 7], [7, 7, 7]),
        ([[[]]], [[]]),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
        (
            [[1, [2, [10, 8, 2, 1, 1]], 0]],
            [
                [[1]],
                [[[2, 4, 10, 2], []], 3, 8],
                [
                    9,
                    3,
                    [5, [3, 0], [0], [4]],
                    6,
                    [[9, 8, 3, 7], 4, [10, 10, 8], 10, [6, 6]],
                ],
                [[[3], 7, [], [10, 5]], 0],
                [5, [[3, 9, 0, 2, 1], 0, [4, 5, 2], [6]]],
            ],
        ),
    ],
)
def test_is_in_order_negative(in_left, in_right):
    """tests is_in_order with input for which the result should be -1"""
    assert sol.is_in_order(in_left, in_right) == -1


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 13, id="small"),
        pytest.param(_data_p(), 5717, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 140, id="small"),
        pytest.param(_data_p(), 25935, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
