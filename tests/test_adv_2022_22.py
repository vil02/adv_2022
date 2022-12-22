"""tests of adv_2022_22"""

import pytest
import general_utils as gu
import solutions.adv_2022_22 as sol

_DAY_NUM = 22


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_parse_input():
    """tests parse input with example data"""
    parse_res = sol.parse_input(_data_small())
    assert parse_res.moves == [10, "R", 5, "L", 5, "R", 10, "L", 4, "R", 5, "L", 5]
    assert parse_res.start_pos == (9, 1)
    assert parse_res.map == {
        (9, 1): ".",
        (10, 1): ".",
        (11, 1): ".",
        (12, 1): "#",
        (9, 2): ".",
        (10, 2): "#",
        (11, 2): ".",
        (12, 2): ".",
        (9, 3): "#",
        (10, 3): ".",
        (11, 3): ".",
        (12, 3): ".",
        (9, 4): ".",
        (10, 4): ".",
        (11, 4): ".",
        (12, 4): ".",
        (1, 5): ".",
        (2, 5): ".",
        (3, 5): ".",
        (4, 5): "#",
        (5, 5): ".",
        (6, 5): ".",
        (7, 5): ".",
        (8, 5): ".",
        (9, 5): ".",
        (10, 5): ".",
        (11, 5): ".",
        (12, 5): "#",
        (1, 6): ".",
        (2, 6): ".",
        (3, 6): ".",
        (4, 6): ".",
        (5, 6): ".",
        (6, 6): ".",
        (7, 6): ".",
        (8, 6): ".",
        (9, 6): "#",
        (10, 6): ".",
        (11, 6): ".",
        (12, 6): ".",
        (1, 7): ".",
        (2, 7): ".",
        (3, 7): "#",
        (4, 7): ".",
        (5, 7): ".",
        (6, 7): ".",
        (7, 7): ".",
        (8, 7): "#",
        (9, 7): ".",
        (10, 7): ".",
        (11, 7): ".",
        (12, 7): ".",
        (1, 8): ".",
        (2, 8): ".",
        (3, 8): ".",
        (4, 8): ".",
        (5, 8): ".",
        (6, 8): ".",
        (7, 8): ".",
        (8, 8): ".",
        (9, 8): ".",
        (10, 8): ".",
        (11, 8): "#",
        (12, 8): ".",
        (9, 9): ".",
        (10, 9): ".",
        (11, 9): ".",
        (12, 9): "#",
        (13, 9): ".",
        (14, 9): ".",
        (15, 9): ".",
        (16, 9): ".",
        (9, 10): ".",
        (10, 10): ".",
        (11, 10): ".",
        (12, 10): ".",
        (13, 10): ".",
        (14, 10): "#",
        (15, 10): ".",
        (16, 10): ".",
        (9, 11): ".",
        (10, 11): "#",
        (11, 11): ".",
        (12, 11): ".",
        (13, 11): ".",
        (14, 11): ".",
        (15, 11): ".",
        (16, 11): ".",
        (9, 12): ".",
        (10, 12): ".",
        (11, 12): ".",
        (12, 12): ".",
        (13, 12): ".",
        (14, 12): ".",
        (15, 12): "#",
        (16, 12): ".",
    }


@pytest.mark.parametrize(
    "input_pos, input_dir, expected",
    [
        ((3, 5), (0, -1), (3, 8)),
        ((1, 5), (-1, 0), (12, 5)),
        ((2, 8), (0, 1), (2, 5)),
        ((12, 5), (1, 0), (1, 5)),
    ],
)
def test_mover_a_wrap_pos(input_pos, input_dir, expected):
    """tests wrap_pos in MoverA"""
    parse_res = sol.parse_input(_data_small())
    mover = sol.MoverA(parse_res.map, parse_res.start_pos)
    assert mover.wrap_pos(input_pos, input_dir) == expected


@pytest.mark.parametrize(
    "input_pos,input_dir,expected",
    [
        ((8, 6), (1, 0), 6032),
        ((7, 5), (0, -1), 5031),
        ((2, 4), (-1, 0), 1000 * 4 + 4 * 2 + 2),
    ],
)
def test_get_pwd(input_pos, input_dir, expected):
    """tests get_pwd"""
    assert sol.get_pwd(input_pos, input_dir) == expected


def test_make_move_mover_a():
    """tests make_move in part a"""
    parse_res = sol.parse_input(_data_small())
    mover = sol.MoverA(parse_res.map, parse_res.start_pos)
    expected = [
        ((11, 1), (1, 0)),
        ((11, 1), (0, 1)),
        ((11, 6), (0, 1)),
        ((11, 6), (1, 0)),
        ((4, 6), (1, 0)),
        ((4, 6), (0, 1)),
        ((4, 8), (0, 1)),
        ((4, 8), (1, 0)),
        ((8, 8), (1, 0)),
        ((8, 8), (0, 1)),
        ((8, 6), (0, 1)),
        ((8, 6), (1, 0)),
    ]

    for cur_move, ex_data in zip(parse_res.moves, expected):
        mover.make_move(cur_move)
        assert (mover.cur_pos, mover.cur_dir) == ex_data


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 6032, id="small"),
        pytest.param(_data_p(), 181128, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


#
#
# @pytest.mark.parametrize(
#     "input_str,expected",
#     [
#         pytest.param(_data_small(), 20, id="small"),
#         pytest.param(_data_p(), 22, id="p"),
#     ],
# )
# def test_solve_b(input_str, expected):
#     """tests solve_b"""
#     assert sol.solve_b(input_str) == expected
