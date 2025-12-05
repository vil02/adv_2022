"""tests of adv_2022_22"""

import pytest
import solutions.adv_2022_22 as sol
from . import test_utils as tu

_INPUTS = tu.get_inputs(22, {"small", "p", "e", "w"})


_DATA_SMALL = _INPUTS.inputs["small"]
assert _DATA_SMALL is not None

_DATA_E = _INPUTS.inputs["e"]
assert _DATA_E is not None

_DATA_W = _INPUTS.inputs["w"]
assert _DATA_W is not None


def test_parse_input():
    """tests parse input with example data"""
    parse_res = sol.parse_input(_DATA_SMALL)
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


def test_mover_wrap_pos_is_abstract():
    """tests if wrap_pos in Mover is not implemented"""
    mover = sol.Mover({(0, 1): "."}, (0, 1))
    with pytest.raises(NotImplementedError):
        mover.wrap_pos((0, 1), (0, 1))


@pytest.mark.parametrize(
    "input_pos, input_dir, expected_pos, expected_dir",
    [
        ((3, 5), (0, -1), (3, 8), (0, -1)),
        ((1, 5), (-1, 0), (12, 5), (-1, 0)),
        ((2, 8), (0, 1), (2, 5), (0, 1)),
        ((12, 5), (1, 0), (1, 5), (1, 0)),
    ],
)
def test_flat_mover_wrap_pos(input_pos, input_dir, expected_pos, expected_dir):
    """tests wrap_pos in FlatMover"""
    parse_res = sol.parse_input(_DATA_SMALL)
    mover = sol.FlatMover(parse_res.map, parse_res.start_pos)
    assert mover.wrap_pos(input_pos, input_dir) == (expected_pos, expected_dir)


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


def test_make_move_flat_mover():
    """tests make_move in part a"""
    parse_res = sol.parse_input(_DATA_SMALL)
    mover = sol.FlatMover(parse_res.map, parse_res.start_pos)
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
        pytest.param(_DATA_SMALL, 4, id="small"),
        pytest.param(_DATA_E, 50, id="e"),
        pytest.param(_DATA_W, 50, id="w"),
    ],
)
def test_compute_side_length(input_str, expected):
    """tests compute_side_length"""
    assert sol.compute_side_length(sol.parse_input(input_str).map) == expected


_SMALL_EDGE_WALKER = sol.EdgeWalker(sol.parse_input(_DATA_SMALL).map)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (9, 1)),
        (_SMALL_EDGE_WALKER, (9, 4)),
        (_SMALL_EDGE_WALKER, (9, 5)),
        (_SMALL_EDGE_WALKER, (8, 5)),
        (_SMALL_EDGE_WALKER, (1, 5)),
        (_SMALL_EDGE_WALKER, (1, 6)),
        (_SMALL_EDGE_WALKER, (16, 12)),
        (_SMALL_EDGE_WALKER, (16, 11)),
        (_SMALL_EDGE_WALKER, (15, 12)),
    ],
)
def test_is_on_edge_positive(edge_walker, pos):
    """positive test of is_on_edge"""
    assert edge_walker.is_on_edge(pos)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (10, 2)),
        (_SMALL_EDGE_WALKER, (10, 2)),
        (_SMALL_EDGE_WALKER, (9, 6)),
        (_SMALL_EDGE_WALKER, (10, 5)),
    ],
)
def test_is_on_edge_negative(edge_walker, pos):
    """negative test of is_on_edge"""
    assert not edge_walker.is_on_edge(pos)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (9, 1)),
        (_SMALL_EDGE_WALKER, (1, 5)),
        (_SMALL_EDGE_WALKER, (1, 8)),
        (_SMALL_EDGE_WALKER, (16, 12)),
    ],
)
def test_is_convex_corner_positive(edge_walker, pos):
    """positive test of is_convex_corner"""
    assert edge_walker.is_convex_corner(pos)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (9, 4)),
        (_SMALL_EDGE_WALKER, (9, 5)),
        (_SMALL_EDGE_WALKER, (8, 5)),
    ],
)
def test_is_convex_corner_negative(edge_walker, pos):
    """negative test of is_convex_corner"""
    assert not edge_walker.is_convex_corner(pos)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (9, 5)),
        (_SMALL_EDGE_WALKER, (9, 8)),
        (_SMALL_EDGE_WALKER, (12, 9)),
    ],
)
def test_is_concave_corner_positive(edge_walker, pos):
    """positive test of is_concave_corner"""
    assert edge_walker.is_concave_corner(pos)


@pytest.mark.parametrize(
    "edge_walker, pos",
    [
        (_SMALL_EDGE_WALKER, (9, 4)),
        (_SMALL_EDGE_WALKER, (8, 5)),
        (_SMALL_EDGE_WALKER, (4, 5)),
        (_SMALL_EDGE_WALKER, (9, 1)),
        (_SMALL_EDGE_WALKER, (13, 9)),
    ],
)
def test_is_concave_corner_negative(edge_walker, pos):
    """negative test of is_concave_corner"""
    assert not edge_walker.is_concave_corner(pos)


@pytest.mark.parametrize(
    "edge_walker, input_walk_data, expected_walk_data",
    [
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((4, 5), (1, 0)),
            sol.WalkData((5, 5), (1, 0)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 1), (0, -1)),
            sol.WalkData((9, 1), (1, 0)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 1), (1, 0)),
            sol.WalkData((10, 1), (1, 0)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 1), (-1, 0)),
            sol.WalkData((9, 1), (0, 1)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 1), (0, 1)),
            sol.WalkData((9, 2), (0, 1)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((8, 8), (1, 0)),
            sol.WalkData((9, 8), (1, 0)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 8), (1, 0)),
            sol.WalkData((9, 8), (0, 1)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 8), (0, 1)),
            sol.WalkData((9, 9), (0, 1)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 9), (0, -1)),
            sol.WalkData((9, 8), (0, -1)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 8), (0, -1)),
            sol.WalkData((9, 8), (-1, 0)),
        ),
        (
            _SMALL_EDGE_WALKER,
            sol.WalkData((9, 8), (-1, 0)),
            sol.WalkData((8, 8), (-1, 0)),
        ),
    ],
)
def test_next_pos(edge_walker, input_walk_data, expected_walk_data):
    """tests next_pos"""
    assert edge_walker.next_pos(input_walk_data) == expected_walk_data


@pytest.mark.parametrize(
    "edge_walker, expected",
    [
        (_SMALL_EDGE_WALKER, {(9, 5), (9, 8), (12, 9)}),
    ],
)
def test_find_all_concave_corners(edge_walker, expected):
    """tests find_all_concave_corners"""
    assert edge_walker.find_all_concave_corners() == expected


@pytest.mark.parametrize(
    "edge_walker, input_pos, expected",
    [
        (_SMALL_EDGE_WALKER, (4, 5), (0, 1)),
        (_SMALL_EDGE_WALKER, (9, 2), (1, 0)),
    ],
)
def test_get_dir_inside(edge_walker, input_pos, expected):
    """tests get_dir_inside"""
    assert edge_walker.get_dir_inside(input_pos) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {
        "small": (6032, 5031),
        "p": (181128, 52311),
        "e": (11464, 197122),
        "w": (186128, 34426),
    },
)
