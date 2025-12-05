"""tests of adv_2022_24"""

import pytest
import solutions.adv_2022_24 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(24, {"small", "p"})


_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


_EXAMPLE_VALLEY = sol.prepare_valley(_DATA_SMALL)
_IS_EMPTY_TEST_SIZE = 20


@pytest.mark.parametrize(
    "in_age, in_pos",
    [
        (0, (2, 0)),
        (0, (2, 1)),
        (1, (3, 0)),
        (1, (0, 0)),
        (6, (2, 2)),
        (10, (2, 2)),
        (12, (2, 2)),
        (13, (2, 2)),
        (16, (0, 0)),
    ],
)
def test_is_empty_positive(in_age, in_pos):
    """positive tests of is_empty method of BlizzardPositions"""
    assert _EXAMPLE_VALLEY.size == (6, 4)
    for _ in range(_IS_EMPTY_TEST_SIZE):
        assert _EXAMPLE_VALLEY.blizzard_positions.is_empty(in_age + 12 * _, in_pos)


@pytest.mark.parametrize(
    "in_age, in_pos",
    [
        (0, (0, 0)),
        (0, (1, 0)),
        (0, (1, 1)),
        (0, (5, 3)),
        (1, (2, 0)),
        (1, (5, 3)),
        (7, (2, 2)),
        (8, (2, 2)),
        (9, (2, 2)),
        (11, (2, 2)),
        (14, (2, 2)),
        (16, (1, 0)),
    ],
)
def test_is_empty_negative(in_age, in_pos):
    """negative tests of is_empty method of BlizzardPositions"""
    assert _EXAMPLE_VALLEY.size == (6, 4)
    for _ in range(_IS_EMPTY_TEST_SIZE):
        assert not _EXAMPLE_VALLEY.blizzard_positions.is_empty(in_age + 12 * _, in_pos)


@pytest.mark.parametrize(
    "input_size, input_pos, expected",
    [
        ((10, 10), (0, 0), {(0, 0), (0, -1), (0, 1), (1, 0)}),
        ((10, 10), (1, 1), {(1, 1), (1, 0), (1, 2), (0, 1), (2, 1)}),
        ((10, 10), (0, -1), {(0, -1), (0, 0)}),
        ((10, 10), (9, 9), {(9, 9), (9, 10), (8, 9), (9, 8)}),
    ],
)
def test_position_candidates(input_size, input_pos, expected):
    """tests position_candidates"""
    assert set(sol.position_candidates(input_size, input_pos)) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (18, 54),
        "p": (221, 739),
    },
)
