"""tests of adv_2022_16"""

import general_utils as gu
import solutions.adv_2022_16 as sol

_DAY_NUM = 16


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse_input with example data"""
    actual = sol.parse_input(_data_small())
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
