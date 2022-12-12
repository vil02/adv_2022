"""tests of adv_2022_11"""

import pytest
import general_utils as gu
import solutions.adv_2022_11 as sol

_DAY_NUM = 11


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _get_dummy_manipulator_b(in_operation):
    return sol.ItemManipulatorB(in_operation, 23)


@pytest.mark.parametrize(
    "get_manipulator",
    [
        pytest.param(sol.ItemManipulatorA, id="sol.ItemManipulatorA"),
        pytest.param(_get_dummy_manipulator_b, id="dummy_manipulator_b"),
    ],
)
def test_parse_input(get_manipulator):
    """tests parse_input with the example data"""
    actual_monkeys, acutal_mod_val = sol.parse_input(_data_small(), get_manipulator)
    expected_monkeys = [
        sol.Monkey(
            [79, 98],
            get_manipulator(sol.get_multiply_by(19)),
            sol.Thrower(23, 2, 3),
        ),
        sol.Monkey(
            [54, 65, 75, 74],
            get_manipulator(sol.get_increase_by(6)),
            sol.Thrower(19, 2, 0),
        ),
        sol.Monkey(
            [79, 60, 97],
            get_manipulator(sol.get_make_square()),
            sol.Thrower(13, 1, 3),
        ),
        sol.Monkey(
            [74], get_manipulator(sol.get_increase_by(3)), sol.Thrower(17, 0, 1)
        ),
    ]
    expected_mod_val = 23 * 19 * 13 * 17
    assert acutal_mod_val == expected_mod_val
    assert all(a == e for a, e in zip(actual_monkeys, expected_monkeys))


def test_make_round():
    """tests make_round with example data"""
    monkeys, _ = sol.parse_input(_data_small(), sol.ItemManipulatorA)
    sol.make_round(monkeys)
    assert len(monkeys) == 4
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


def test_make_rounds():
    """tests make_rounds with example data"""
    monkeys, _ = sol.parse_input(_data_small(), sol.ItemManipulatorA)
    sol.make_rounds(monkeys, 20)
    assert len(monkeys) == 4
    assert monkeys[0].inspected_items == 101
    assert monkeys[1].inspected_items == 95
    assert monkeys[2].inspected_items == 7
    assert monkeys[3].inspected_items == 105


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 10605, id="small"),
        pytest.param(_data_p(), 78960, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 2713310158, id="small"),
        pytest.param(_data_p(), 14561971968, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
