"""tests of adv_2022_02"""

import solutions.adv_2022_02 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(2, {"small", "p", "s", "b", "t"})


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (15, 12),
        "p": (10941, 13071),
        "s": (11666, 12767),
        "b": (12276, 9975),
        "t": (14375, 10274),
    },
)
