"""tests of adv_2022_18"""

import solutions.adv_2022_18 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(18, {"small", "my_1", "my_2", "my_3", "p", "s"})


_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input with example data"""
    expected = (
        (2, 2, 2),
        (1, 2, 2),
        (3, 2, 2),
        (2, 1, 2),
        (2, 3, 2),
        (2, 2, 1),
        (2, 2, 3),
        (2, 2, 4),
        (2, 2, 6),
        (1, 2, 5),
        (3, 2, 5),
        (2, 1, 5),
        (2, 3, 5),
    )
    assert sol.parse_input(_DATA_SMALL) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "my_1": (6 * 3 * 3 + 6, 6 * 3 * 3),
        "my_2": (2 * 9 + 4 * 3 * 4 + 10, 2 * 9 + 4 * 3 * 4),
        "my_3": (2 * 9 + 4 * 3 * 5 + 2 * 6, 2 * 9 + 4 * 3 * 5),
        "small": (64, 58),
        "p": (4348, 2546),
        "s": (3364, 2006),
    },
)
