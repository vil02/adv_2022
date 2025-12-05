"""tests of adv_2022_17"""

import solutions.adv_2022_17 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(17, {"small", "blocks", "p"})
_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None

_DATA_BLOCKS = _INPUTS.inputs["blocks"]
assert _DATA_BLOCKS is not None


def test_parse_blocks():
    """tests parse_blocks"""
    expected = (
        frozenset({(0, 0), (1, 0), (2, 0), (3, 0)}),
        frozenset({(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)}),
        frozenset({(2, 1), (0, 0), (2, 0), (2, 2), (1, 0)}),
        frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
        frozenset({(0, 0), (1, 0), (0, 1), (1, 1)}),
    )
    assert sol.parse_blocks(_DATA_BLOCKS) == expected


def test_parse_input():
    """tests parse input with example data"""
    expected = (
        ">",
        ">",
        ">",
        "<",
        "<",
        ">",
        "<",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        "<",
        ">",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        ">",
        "<",
        "<",
        "<",
        ">",
        "<",
        "<",
        "<",
        ">",
        ">",
        "<",
        ">",
        ">",
        "<",
        "<",
        ">",
        ">",
    )
    assert sol.parse_input(_DATA_SMALL) == expected


def test_drop_single_returns_none_when_generator_exhausted():
    """checks that drop_single returns None when gen_moves exhausted"""

    def _move_generator():
        yield "<"
        yield "<"

    assert sol.drop_single(set(), {(0, 0), (0, 1)}, _move_generator()) is None


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (3068, 1514285714288),
        "p": (3181, 1570434782634),
    },
)
