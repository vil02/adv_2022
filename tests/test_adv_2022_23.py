"""tests of adv_2022_23"""

import pytest
import general_utils as gu
import solutions.adv_2022_23 as sol

_DAY_NUM = 23


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_very_small():
    return gu.read_input(_DAY_NUM, "very_small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_single_round():
    """tests single_round with very_small example data"""
    elves = [sol.Elf(_) for _ in sol.parse_input(_data_very_small())]
    dir_names = [sol.get_dir_name(_) for _ in range(4)]
    for _ in range(3):
        sol.single_round(elves, dir_names)
        expected_positions = sol.parse_input(
            gu.read_input(_DAY_NUM, f"very_small_{_+1}")
        )
        actual_positions = frozenset(_.pos for _ in elves)

        assert actual_positions == expected_positions


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 110, id="small"),
        pytest.param(_data_p(), 3757, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 20, id="small"),
        pytest.param(_data_p(), 918, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
