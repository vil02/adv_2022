"""tests of adv_2022_05"""

import pytest
import solutions.adv_2022_05 as sol
from . import test_utils as tu


@pytest.mark.parametrize(
    "input_col,expected",
    [
        (1, 1),
        (5, 2),
        (9, 3),
    ],
)
def test_get_stack_number(input_col, expected):
    """tests get_stack_number"""
    assert sol.get_stack_number(input_col) == expected


_INPUTS = tu.get_inputs(5, {"small", "p", "s", "b", "t"})
_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input"""
    actual_state, actual_moves = sol.parse_input(_DATA_SMALL)
    expected_state = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}
    expected_moves = [
        sol.Move(1, 2, 1),
        sol.Move(3, 1, 3),
        sol.Move(2, 2, 1),
        sol.Move(1, 1, 2),
    ]
    assert actual_state == expected_state
    assert actual_moves == expected_moves


@pytest.mark.parametrize(
    "input_str,move_fun,expected_state",
    [
        pytest.param(
            _DATA_SMALL,
            sol.make_move_a,
            {1: ["C"], 2: ["M"], 3: ["P", "D", "N", "Z"]},
            id="small_with_make_move_a",
        ),
        pytest.param(
            _DATA_SMALL,
            sol.make_move_b,
            {1: ["M"], 2: ["C"], 3: ["P", "Z", "N", "D"]},
            id="small_with_make_move_b",
        ),
    ],
)
def test_make_move(input_str, move_fun, expected_state):
    """tests make_move"""
    state, moves = sol.parse_input(input_str)
    sol.make_moves(state, moves, move_fun)
    assert state == expected_state


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": ("CMZ", "MCD"),
        "p": ("LJSVLTWQM", "BRQWDBBJM"),
        "s": ("TQRFCBSJJ", "RMHFJNVFP"),
        "b": ("SHMSDGZVC", "VRZGHDFBQ"),
        "t": ("RNZLFZSJH", "CNSFCGJSM"),
    },
)
