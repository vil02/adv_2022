"""tests of adv_2022_19"""

import pytest
import general_utils as gu
import solutions.adv_2022_19 as sol

_DAY_NUM = 19


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse input with example data"""
    expected = (
        sol.Blueprint(
            1,
            {
                "ore": {"ore": 4},
                "clay": {"ore": 2},
                "obsidian": {"ore": 3, "clay": 14},
                "geode": {"ore": 2, "obsidian": 7},
            },
        ),
        sol.Blueprint(
            2,
            {
                "ore": {"ore": 2},
                "clay": {"ore": 3},
                "obsidian": {"ore": 3, "clay": 8},
                "geode": {"ore": 3, "obsidian": 12},
            },
        ),
    )
    assert sol.parse_input(_data_small()) == expected


@pytest.mark.parametrize(
    "input_id,input_max_genodes,expected",
    [
        (2, 6, 12),
        (1, 9, 9),
        (2, 12, 24),
    ],
)
def test_compute_quality_level(input_id, input_max_genodes, expected):
    """tests compute_quality_level"""
    assert sol.compute_quality_level(input_id, input_max_genodes) == expected
