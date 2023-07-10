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
    "input_resources,input_robot_cost,expected",
    [
        ((3, 4, 3, 1), (1, 1, 1, 1), (0, 0, 0, 0)),
        ((3, 4, 3, 1), (1, 5, 1, 1), (0, 1, 0, 0)),
        ((1, 2, 3, 4), (3, 3, 3, 3), (2, 1, 0, 0)),
    ],
)
def test_compute_needed_resources(input_resources, input_robot_cost, expected):
    """tests compute_needed_resources"""
    assert sol.compute_needed_resources(input_resources, input_robot_cost) == expected


@pytest.mark.parametrize(
    "in_production_rate, in_needed_amout, expected",
    [
        (0, 0, 0),
        (0, 1, math.inf),
        (5, 5, 1),
        (6, 5, 1),
        (5, 6, 2),
        (3, 2, 1),
        (3, 3, 1),
        (3, 4, 2),
        (3, 5, 2),
        (3, 6, 2),
        (3, 7, 3),
        (3, 8, 3),
        (3, 9, 3),
        (3, 10, 4),
    ],
)
def test_compute_waiting_time_for_single(in_production_rate, in_needed_amout, expected):
    """tests compute_waiting_time_for_single"""
    assert (
        sol.compute_waiting_time_for_single(in_production_rate, in_needed_amout)
        == expected
    )


@pytest.mark.parametrize(
    "in_production_rates, in_needed_resources, expected",
    [
        ((1, 0, 0, 0), (2, 0, 0, 0), 2),
        ((1, 0, 0, 0), (2, 0, 0, 1), math.inf),
        ((1, 0, 0, 5), (2, 0, 0, 1), 2),
    ],
)
def test_compute_waiting_time(in_production_rates, in_needed_resources, expected):
    """tests compute_waiting_time"""
    assert (
        sol.compute_waiting_time(in_production_rates, in_needed_resources) == expected
    )


def _parse_to_raw(in_data, in_num):
    return sol.blueprint_to_raw_format(sol.parse_input(in_data)[in_num])


_RAW_BLUEPRINT_P_1 = _parse_to_raw(_data_p(), 0)
_RAW_BLUEPRINT_P_2 = _parse_to_raw(_data_p(), 1)
_RAW_BLUEPRINT_P_3 = _parse_to_raw(_data_p(), 2)


@pytest.mark.parametrize(
    "input_raw_blueprint,input_time_limit,expected",
    [
        (_RAW_BLUEPRINT_SMALL_1, 19, 1),
        (_RAW_BLUEPRINT_SMALL_1, 20, 2),
        (_RAW_BLUEPRINT_SMALL_1, 24, 9),
        # (_RAW_BLUEPRINT_SMALL_1, 32, 56),
        (_RAW_BLUEPRINT_SMALL_2, 19, 1),
        (_RAW_BLUEPRINT_SMALL_2, 20, 2),
        (_RAW_BLUEPRINT_SMALL_2, 24, 12),
        # (_RAW_BLUEPRINT_SMALL_2, 32, 62),
        (_RAW_BLUEPRINT_P_1, 24, 3),
        (_RAW_BLUEPRINT_P_1, 32, 38),
        (_RAW_BLUEPRINT_P_2, 24, 0),
        (_RAW_BLUEPRINT_P_2, 32, 10),
        (_RAW_BLUEPRINT_P_3, 24, 1),
        (_RAW_BLUEPRINT_P_3, 32, 18),
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
