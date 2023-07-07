"""tests of adv_2022_19"""

import math
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


_RAW_BLUEPRINT_SMALL_1 = ((4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0))
_RAW_BLUEPRINT_SMALL_2 = ((2, 0, 0, 0), (3, 0, 0, 0), (3, 8, 0, 0), (3, 0, 12, 0))


@pytest.mark.parametrize(
    "input_blueprint,expected",
    [
        (sol.parse_input(_data_small())[0], _RAW_BLUEPRINT_SMALL_1),
        (sol.parse_input(_data_small())[1], _RAW_BLUEPRINT_SMALL_2),
    ],
)
def test_blueprint_to_raw_format(input_blueprint, expected):
    """tests blueprint_to_raw_formar"""
    assert sol.blueprint_to_raw_format(input_blueprint) == expected


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


@pytest.mark.parametrize(
    "input_raw_blueprint,expected",
    [
        (_RAW_BLUEPRINT_SMALL_1, (4, 14, 7, math.inf)),
        (_RAW_BLUEPRINT_SMALL_2, (3, 8, 12, math.inf)),
    ],
)
def test_get_bounds(input_raw_blueprint, expected):
    """tests get_bounds"""
    assert sol.get_bounds(input_raw_blueprint) == expected


@pytest.mark.parametrize(
    "input_raw_blueprint,input_time_limit,expected",
    [
        (_RAW_BLUEPRINT_SMALL_1, 19, 1),
        (_RAW_BLUEPRINT_SMALL_1, 20, 2),
        (_RAW_BLUEPRINT_SMALL_1, 24, 9),
        (_RAW_BLUEPRINT_SMALL_1, 32, 56),
        (_RAW_BLUEPRINT_SMALL_2, 19, 1),
        (_RAW_BLUEPRINT_SMALL_2, 20, 2),
        (_RAW_BLUEPRINT_SMALL_2, 24, 12),
        (_RAW_BLUEPRINT_SMALL_2, 32, 62),
    ],
)
def test_evaluate_blueprint(input_raw_blueprint, input_time_limit, expected):
    """tests evaluate_blueprint"""
    assert sol.evaluate_blueprint(input_raw_blueprint, input_time_limit) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 33, id="small"),
        pytest.param(_data_p(), 1675, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_p(), 6840, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
