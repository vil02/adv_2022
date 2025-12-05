"""tests of adv_2022_00"""

import solutions.adv_2022_21 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(21, {"small", "p"})


_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input with example data"""
    expected = {
        "root": sol.Operation(operation="+", register_a="pppw", register_b="sjmn"),
        "dbpl": 5,
        "cczh": sol.Operation(operation="+", register_a="sllz", register_b="lgvd"),
        "zczc": 2,
        "ptdq": sol.Operation(operation="-", register_a="humn", register_b="dvpt"),
        "dvpt": 3,
        "lfqf": 4,
        "humn": 5,
        "ljgn": 2,
        "sjmn": sol.Operation(operation="*", register_a="drzm", register_b="dbpl"),
        "sllz": 4,
        "pppw": sol.Operation(operation="/", register_a="cczh", register_b="lfqf"),
        "lgvd": sol.Operation(operation="*", register_a="ljgn", register_b="ptdq"),
        "drzm": sol.Operation(operation="-", register_a="hmdt", register_b="zczc"),
        "hmdt": 32,
    }
    assert sol.parse_input(_DATA_SMALL) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (152, 301),
        "p": (331319379445180, 3715799488132),
    },
)
