"""tests of adv_2022_00"""

import solutions.adv_2022_00 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(0, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (10, 20), "p": (11, 22)}
)
