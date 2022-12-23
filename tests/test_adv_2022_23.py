"""tests of adv_2022_23"""

import pytest
import general_utils as gu
import solutions.adv_2022_23 as sol

_DAY_NUM = 23


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_bigger():
    return gu.read_input(_DAY_NUM, "bigger")


def _data_very_small():
    return gu.read_input(_DAY_NUM, "very_small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "data_postfix, round_limit",
    [("very_small", 3), ("bigger", 5)],
)
def test_single_round(data_postfix, round_limit):
    """tests single_round with very_small example data"""
    elves_mover = sol.ElvesMover(
        sol.parse_input(gu.read_input(_DAY_NUM, f"{data_postfix}"))
    )
    for _ in range(round_limit):
        elves_mover.single_round()
        expected_positions = sol.parse_input(
            gu.read_input(_DAY_NUM, f"{data_postfix}_{_+1}")
        )

        assert elves_mover.positions == expected_positions


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 110, id="small"),
        pytest.param(_data_bigger(), 110, id="bigger"),
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
        pytest.param(_data_bigger(), 20, id="bigger"),
        pytest.param(_data_p(), 918, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
