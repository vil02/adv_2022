"""tests of adv_2022_23"""

import pytest
import solutions.adv_2022_23 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(
    23,
    {
        "small",
        "bigger",
        "bigger_1",
        "bigger_2",
        "bigger_3",
        "bigger_4",
        "bigger_5",
        "very_small",
        "very_small_1",
        "very_small_2",
        "very_small_3",
        "p",
    },
)


@pytest.mark.parametrize(
    "data_postfix, round_limit",
    [("very_small", 3), ("bigger", 5)],
)
def test_single_round(data_postfix, round_limit):
    """tests single_round with very_small example data"""
    elves_mover = sol.ElvesMover(sol.parse_input(_INPUTS.inputs[data_postfix]))
    for _ in range(round_limit):
        elves_mover.single_round()
        expected_positions = sol.parse_input(_INPUTS.inputs[data_postfix + f"_{_ + 1}"])

        assert elves_mover.positions == expected_positions


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (110, 20),
        "bigger": (110, 20),
        "p": (3757, 918),
    },
)
