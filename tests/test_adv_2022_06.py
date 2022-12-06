"""tests of adv_2022_06"""

import pytest
import general_utils as gu
import solutions.adv_2022_06 as sol

_DAY_NUM = 6


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _get_id(in_part, in_num):
    return f"example_{in_part}_{in_num}"


@pytest.mark.parametrize(
    "input_str,block_size,expected",
    [
        ("1234X", 4, 4),
        ("11234", 4, 5),
        ("1", 1, 1),
        ("12", 2, 2),
    ],
)
def test_find_first_block_end(input_str, block_size, expected):
    """tests find_first_block_end"""
    assert sol.find_first_block_end(input_str, block_size) == expected


@pytest.mark.parametrize(
    "input_str,block_size",
    [
        ("ABCABCABC", 4),
        ("AB", 3),
    ],
)
def test_find_first_block_end_raises_exception_when_block_not_found(
    input_str, block_size
):
    """
    tests find_first_block_end raises an exception
    if block of distinct characters cannot be found
    """
    with pytest.raises(ValueError):
        sol.find_first_block_end(input_str, block_size)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, id=_get_id("a", 0)),
        pytest.param("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, id=_get_id("a", 1)),
        pytest.param("nppdvjthqldpwncqszvftbrmjlhg", 6, id=_get_id("a", 2)),
        pytest.param("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, id=_get_id("a", 3)),
        pytest.param("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, id=_get_id("a", 4)),
        pytest.param(_data_p(), 1816),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19, id=_get_id("a", 0)),
        pytest.param("bvwbjplbgvbhsrlpgdmjqwftvncz", 23, id=_get_id("a", 1)),
        pytest.param("nppdvjthqldpwncqszvftbrmjlhg", 23, id=_get_id("a", 2)),
        pytest.param("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29, id=_get_id("a", 3)),
        pytest.param("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26, id=_get_id("a", 4)),
        pytest.param(_data_p(), 2625, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
