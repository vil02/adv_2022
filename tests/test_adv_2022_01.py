"""tests of adv_2022_01"""

import solutions.adv_2022_01 as sol
from . import test_utils as tu


_INPUTS = tu.get_inputs(1, {"small", "p", "f", "b", "t"})


def test_parse_input():
    """tests parse_input against example data"""
    expected = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    data_small = _INPUTS.inputs["small"]
    assert data_small is not None
    actual = sol.parse_input(data_small)
    assert expected == actual


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (24000, 45000),
        "p": (69912, 208180),
        "f": (66487, 197301),
        "b": (68923, 200044),
        "t": (68802, 205370),
    },
)
