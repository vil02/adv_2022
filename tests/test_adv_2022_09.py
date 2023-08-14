"""tests of adv_2022_09"""

import pytest
import general_utils as gu
import solutions.adv_2022_09 as sol

_DAY_NUM = 9


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_bigger():
    return gu.read_input(_DAY_NUM, "bigger")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


def _data_b():
    return gu.read_input(_DAY_NUM, "b")


def test_parse_input():
    """tests parse input with example data"""
    actual = sol.parse_input(_data_small())
    expected = [
        sol.Move("R", 4),
        sol.Move("U", 4),
        sol.Move("L", 3),
        sol.Move("D", 1),
        sol.Move("R", 4),
        sol.Move("D", 1),
        sol.Move("L", 5),
        sol.Move("R", 2),
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "input_head,input_tail,expected",
    [
        ((2, 2), (2, 2), (2, 2)),
        ((2, 2), (1, 1), (1, 1)),
        ((3, 1), (1, 1), (2, 1)),
        ((1, 1), (1, 3), (1, 2)),
        ((2, 3), (1, 1), (2, 2)),
        ((3, 2), (1, 1), (2, 2)),
    ],
)
def test_move_tail(input_head, input_tail, expected):
    """tests move_tail"""
    assert sol.move_tail(input_head, input_tail) == expected


@pytest.mark.parametrize(
    "input_str,rope_length,expected",
    [
        pytest.param(
            _data_small(),
            2,
            {
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 1),
                (4, 2),
                (3, 2),
                (2, 2),
                (1, 2),
                (3, 3),
                (4, 3),
                (2, 4),
                (3, 4),
            },
            id="small",
        ),
        pytest.param(
            _data_bigger(),
            10,
            {
                (0, 0),
                (1, 1),
                (2, 2),
                (1, 3),
                (2, 4),
                (3, 5),
                (4, 5),
                (5, 5),
                (6, 4),
                (7, 3),
                (8, 2),
                (9, 1),
                (10, 0),
                (9, -1),
                (8, -2),
                (7, -3),
                (6, -4),
                (5, -5),
                (4, -5),
                (3, -5),
                (2, -5),
                (1, -5),
                (0, -5),
                (-1, -5),
                (-2, -5),
                (-3, -4),
                (-4, -3),
                (-5, -2),
                (-6, -1),
                (-7, 0),
                (-8, 1),
                (-9, 2),
                (-10, 3),
                (-11, 4),
                (-11, 5),
                (-11, 6),
            },
            id="bigger",
        ),
    ],
)
def test_rope_simulator(input_str, rope_length, expected):
    """tests RopeSimulator"""
    rope_simulator = sol.RopeSimulator(rope_length)
    rope_simulator.make_moves(sol.parse_input(input_str))
    assert rope_simulator.visited_by_tail == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 13, id="small"),
        pytest.param(_data_p(), 6090, id="p"),
        pytest.param(_data_s(), 6011, id="s"),
        pytest.param(_data_b(), 6243, id="b"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 1, id="small"),
        pytest.param(_data_bigger(), 36, id="bigger"),
        pytest.param(_data_p(), 2566, id="p"),
        pytest.param(_data_s(), 2419, id="s"),
        pytest.param(_data_b(), 2630, id="b"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
