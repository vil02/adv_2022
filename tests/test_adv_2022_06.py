"""tests of adv_2022_06"""

import pytest
import solutions.adv_2022_06 as sol
from . import test_utils as tu


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


_INPUTS = tu.get_inputs(
    6, {"small_0", "small_1", "small_2", "small_3", "small_4", "p", "g", "b", "t"}
)

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small_0": (7, 19),
        "small_1": (5, 23),
        "small_2": (6, 23),
        "small_3": (10, 29),
        "small_4": (11, 26),
        "p": (1816, 2625),
        "g": (1140, 3495),
        "b": (1210, 3476),
        "t": (1235, 3051),
    },
)
