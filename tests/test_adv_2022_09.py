"""tests of adv_2022_09"""

import pytest
import solutions.adv_2022_09 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(9, {"small", "bigger", "p", "s", "b"})

_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None

_DATA_BIGGER = _INPUTS.inputs["bigger"]
assert _DATA_BIGGER is not None


def test_parse_input():
    """tests parse input with example data"""
    actual = sol.parse_input(_DATA_SMALL)
    expected = [
        sol.Move("R", 4),
        sol.Move("U", 4),
        sol.Move("L", 3),
        sol.Move("D", 1),
        sol.Move("R", 4),
        sol.Move("D", 1),
        sol.Move("L", 5),
        sol.Move("R", 2),
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "input_head,input_tail,expected",
    [
        ((2, 2), (2, 2), (2, 2)),
        ((2, 2), (1, 1), (1, 1)),
        ((3, 1), (1, 1), (2, 1)),
        ((1, 1), (1, 3), (1, 2)),
        ((2, 3), (1, 1), (2, 2)),
        ((3, 2), (1, 1), (2, 2)),
    ],
)
def test_move_tail(input_head, input_tail, expected):
    """tests move_tail"""
    assert sol.move_tail(input_head, input_tail) == expected


@pytest.mark.parametrize(
    "input_str,rope_length,expected",
    [
        pytest.param(
            _DATA_SMALL,
            2,
            {
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 1),
                (4, 2),
                (3, 2),
                (2, 2),
                (1, 2),
                (3, 3),
                (4, 3),
                (2, 4),
                (3, 4),
            },
            id="small",
        ),
        pytest.param(
            _DATA_BIGGER,
            10,
            {
                (0, 0),
                (1, 1),
                (2, 2),
                (1, 3),
                (2, 4),
                (3, 5),
                (4, 5),
                (5, 5),
                (6, 4),
                (7, 3),
                (8, 2),
                (9, 1),
                (10, 0),
                (9, -1),
                (8, -2),
                (7, -3),
                (6, -4),
                (5, -5),
                (4, -5),
                (3, -5),
                (2, -5),
                (1, -5),
                (0, -5),
                (-1, -5),
                (-2, -5),
                (-3, -4),
                (-4, -3),
                (-5, -2),
                (-6, -1),
                (-7, 0),
                (-8, 1),
                (-9, 2),
                (-10, 3),
                (-11, 4),
                (-11, 5),
                (-11, 6),
            },
            id="bigger",
        ),
    ],
)
def test_rope_simulator(input_str, rope_length, expected):
    """tests RopeSimulator"""
    rope_simulator = sol.RopeSimulator(rope_length)
    rope_simulator.make_moves(sol.parse_input(input_str))
    assert rope_simulator.visited_by_tail == expected


test_solve_a = _INPUTS.get_test(
    sol.solve_a,
    {
        "small": 13,
        "p": 6090,
        "s": 6011,
        "b": 6243,
    },
)

test_solve_b = _INPUTS.get_test(
    sol.solve_b,
    {
        "small": 1,
        "bigger": 36,
        "p": 2566,
        "s": 2419,
        "b": 2630,
    },
)
