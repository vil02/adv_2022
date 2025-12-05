"""tests of adv_2022_04"""

import pytest
import solutions.adv_2022_04 as sol
from . import test_utils as tu


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


_INPUTS = tu.get_inputs(4, {"small", "p", "s", "b", "t"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (2, 4),
        "p": (433, 852),
        "s": (582, 893),
        "b": (462, 835),
        "t": (524, 798),
    },
)
