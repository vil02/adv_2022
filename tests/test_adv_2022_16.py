"""tests of adv_2022_16"""

import pytest
import solutions.adv_2022_16 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(16, {"small", "p"})
_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_DATA_SMALL)
    expected = {
        "AA": sol.Valve(flow_rate=0, targets={"DD", "BB", "II"}),
        "BB": sol.Valve(flow_rate=13, targets={"CC", "AA"}),
        "CC": sol.Valve(flow_rate=2, targets={"DD", "BB"}),
        "DD": sol.Valve(flow_rate=20, targets={"EE", "CC", "AA"}),
        "EE": sol.Valve(flow_rate=3, targets={"DD", "FF"}),
        "FF": sol.Valve(flow_rate=0, targets={"EE", "GG"}),
        "GG": sol.Valve(flow_rate=0, targets={"HH", "FF"}),
        "HH": sol.Valve(flow_rate=22, targets={"GG"}),
        "II": sol.Valve(flow_rate=0, targets={"JJ", "AA"}),
        "JJ": sol.Valve(flow_rate=21, targets={"II"}),
    }

    assert actual == expected


@pytest.mark.parametrize(
    "input_valves, start_valve, expected",
    [
        (
            sol.parse_input(_DATA_SMALL),
            "AA",
            {
                "AA": 0,
                "BB": 1,
                "CC": 2,
                "DD": 1,
                "EE": 2,
                "FF": 3,
                "GG": 4,
                "HH": 5,
                "II": 1,
                "JJ": 2,
            },
        ),
    ],
)
def test_compute_distances(input_valves, start_valve, expected):
    """tests compute_distances"""
    assert sol.compute_distances(input_valves, start_valve) == expected


@pytest.mark.parametrize(
    "input_mask, input_bit_num, expected",
    [
        (0, 0, False),
        (0, 1, False),
        (0, 2, False),
        (0, 3, False),
        (0, 4, False),
        (1, 0, True),
        (1, 1, False),
        (1, 1, False),
        (2, 0, False),
        (2, 1, True),
        (2, 2, False),
        (13, 0, True),
        (13, 1, False),
        (13, 2, True),
        (13, 3, True),
        (13, 4, False),
    ],
)
def test_is_nth_bit_set(input_mask, input_bit_num, expected):
    """tests is_nth_bit_set"""
    assert sol.is_nth_bit_set(input_mask, input_bit_num) == expected


@pytest.mark.parametrize(
    "in_valves, expected",
    [
        (sol.parse_input(_DATA_SMALL), {"BB", "CC", "DD", "EE", "HH", "JJ"}),
    ],
)
def test_get_openable_valves(in_valves, expected):
    """ "tests get_openable_valves"""
    assert sol.get_openable_valves(in_valves) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (1651, 1707),
        "p": (1862, 2422),
    },
)
