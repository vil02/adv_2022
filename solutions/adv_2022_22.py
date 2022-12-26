"""solution of adv_2022_22"""

import collections
import string
import math


def _to_pos(in_x, in_y):
    return (in_x, in_y)


def _parse_map(in_str):
    map_data = {}
    start_pos = None
    for pos_y, row in enumerate(in_str.splitlines(), start=1):
        for pos_x, cur_char in enumerate(row, start=1):
            if cur_char != " ":
                if start_pos is None:
                    assert cur_char != "#"
                    start_pos = _to_pos(pos_x, pos_y)
                assert cur_char in {".", "#"}
                map_data[_to_pos(pos_x, pos_y)] = cur_char
    assert start_pos is not None
    return map_data, start_pos


def _parse_moves(in_str):
    def _to_int(in_num_chars):
        return int("".join(in_num_chars))

    res = []
    cur_num_chars = []
    for _ in in_str:
        if _ in {"L", "R"}:
            res.append(_to_int(cur_num_chars))
            cur_num_chars = []
            res.append(_)
        else:
            assert _ in string.digits
            cur_num_chars.append(_)
    assert cur_num_chars
    res.append(_to_int(cur_num_chars))
    return res


def parse_input(in_str):
    """parses the input"""
    map_str, moves_str = in_str.split("\n\n")
    map_data, start_pos = _parse_map(map_str)
    return collections.namedtuple("ParsingResult", ["map", "start_pos", "moves"])(
        map_data, start_pos, _parse_moves(moves_str.strip())
    )


def _change_dir(in_dir, in_turn):
    new_dirs = {
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
    }
    if in_turn == "R":
        new_dirs = {val: key for key, val in new_dirs.items()}
    else:
        assert in_turn == "L"
    return new_dirs[in_dir]


def _add_tuples(*in_tuples):
    return tuple(sum(_) for _ in zip(*in_tuples))


def _make_shift(in_pos, in_shift):
    return _add_tuples(in_pos, in_shift)


def _multiply_tuple(in_scalar, in_tuple):
    return tuple(in_scalar * _ for _ in in_tuple)


def _negate_tuple(in_tuple):
    return _multiply_tuple(-1, in_tuple)


class _Mover:
    def __init__(self, map_data, start_pos):
        self._map = map_data
        self._cur_pos = start_pos
        self._cur_dir = (1, 0)

    def wrap_pos(self, in_pos, in_dir):
        """returns the position/direction after the move outside"""
        raise NotImplementedError()

    def _change_dir(self, in_turn):
        self._cur_dir = _change_dir(self.cur_dir, in_turn)

    def _is_empty(self, in_pos):
        return self._map[in_pos] == "."

    def _single_step(self):
        new_pos = _make_shift(self.cur_pos, self.cur_dir)
        if new_pos in self._map:
            if self._is_empty(new_pos):
                self._cur_pos = new_pos
            return
        wraped_pos, wraped_dir = self.wrap_pos(self.cur_pos, self.cur_dir)
        if self._is_empty(wraped_pos):
            self._cur_pos = wraped_pos
            self._cur_dir = wraped_dir

    def make_move(self, in_move):
        """makes the single move"""
        if in_move in {"L", "R"}:
            self._change_dir(in_move)
        else:
            for _ in range(in_move):
                self._single_step()

    def make_moves(self, in_moves):
        """makes all of the moves in_moves"""
        for _ in in_moves:
            self.make_move(_)

    @property
    def cur_pos(self):
        """getter for _cur_pos"""
        return self._cur_pos

    @property
    def cur_dir(self):
        """getter for _cur_dir"""
        return self._cur_dir


class MoverFlat(_Mover):
    """imlements a _Mover class for a walk on a flat map"""

    def __init__(self, map_data, start_pos):
        super().__init__(map_data, start_pos)
        self._wraps = {}

    def wrap_pos(self, in_pos, in_dir):
        """wraps the position as in part a"""
        assert in_pos in self._map
        if (in_pos, in_dir) in self._wraps:
            return self._wraps[(in_pos, in_dir)]
        search_dir = _negate_tuple(in_dir)
        tmp_pos = in_pos
        while tmp_pos in self._map:
            tmp_pos = _make_shift(tmp_pos, search_dir)
        res = _make_shift(tmp_pos, in_dir), in_dir
        self._wraps[(in_pos, in_dir)] = res
        return res


def _facing(in_dir):
    return {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[in_dir]


def get_pwd(in_pos, in_dir):
    """returns the password of given positon/direction"""
    return 1000 * in_pos[1] + 4 * in_pos[0] + _facing(in_dir)


def _solve(in_str, mover_type):
    parse_res = parse_input(in_str)
    mover = mover_type(parse_res.map, parse_res.start_pos)
    mover.make_moves(parse_res.moves)
    return get_pwd(mover.cur_pos, mover.cur_dir)


def solve_a(in_str):
    """returns the solution for part_a"""
    return _solve(in_str, MoverFlat)


def _get_all_dirs():
    return (
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    )


def _get_main_dirs():
    return (
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    )


def _calculate_maxs(in_map):
    x_max = 0
    y_max = 0
    for x_pos, y_pos in in_map:
        x_max = max(x_max, x_pos)
        y_max = max(y_max, y_pos)
    return x_max, y_max


def compute_side_length(in_net):
    """returns the length of the cube with net represented by in_net"""
    side_length = math.gcd(*_calculate_maxs(in_net))
    assert len(in_net) == 6 * side_length**2
    return side_length


WalkData = collections.namedtuple("WalkData", ["pos", "dir"])


class EdgeWalker:
    """
    implements functionalities related to moving along the edges of a net of a cube
    """

    def __init__(self, in_net):
        assert compute_side_length(in_net) >= 2
        self.net = in_net

    def is_in(self, in_pos):
        """returns True iff in_pos is inside the net"""
        return in_pos in self.net

    def _is_shift_in(self, in_pos, in_shift):
        return self.is_in(_make_shift(in_pos, in_shift))

    def _is_shift_on_edge(self, in_pos, in_shift):
        return self.is_on_edge(_make_shift(in_pos, in_shift))

    def is_on_edge(self, in_pos):
        """checks if given position is on the edge of the net"""
        assert in_pos in self.net
        return any(not self._is_shift_in(in_pos, _) for _ in _get_all_dirs())

    def is_convex_corner(self, in_pos):
        """checks if in_pos is on a outer/convex corner"""
        assert self.is_on_edge(in_pos)
        return sum(1 for _ in _get_all_dirs() if self._is_shift_in(in_pos, _)) == 3

    def is_concave_corner(self, in_pos):
        """checks if in_pos is on a inner/concave corner"""
        assert self.is_on_edge(in_pos)
        return sum(1 for _ in _get_all_dirs() if self._is_shift_in(in_pos, _)) == 7

    def get_edge_dirs(self, in_pos):
        """returns all directions along the edges at given position"""
        assert self.is_on_edge(in_pos)
        return [
            _
            for _ in _get_main_dirs()
            if self._is_shift_in(in_pos, _) and self._is_shift_on_edge(in_pos, _)
        ]

    def get_dir_inside(self, in_pos):
        """
        Returns a direction "inside" the cubes net.
        in_pos cannot be on the corner.
        """
        assert (
            self.is_on_edge(in_pos)
            and not self.is_convex_corner(in_pos)
            and not self.is_concave_corner(in_pos)
        )
        dirs = [
            _
            for _ in _get_main_dirs()
            if self._is_shift_in(in_pos, _) and not self._is_shift_on_edge(in_pos, _)
        ]
        assert len(dirs) == 1
        return dirs[0]

    def next_pos(self, in_walk_data):
        """returns the data describing the next position in a walk along the edge"""
        assert self.is_on_edge(in_walk_data.pos)
        next_pos = _make_shift(in_walk_data.pos, in_walk_data.dir)
        if self.is_in(next_pos) and self.is_on_edge(next_pos):
            return WalkData(next_pos, in_walk_data.dir)
        edge_dirs = self.get_edge_dirs(in_walk_data.pos)
        assert len(edge_dirs) == 2
        assert self.is_concave_corner(in_walk_data.pos) or self.is_convex_corner(
            in_walk_data.pos
        )
        edge_dirs.remove(_negate_tuple(in_walk_data.dir))
        return WalkData(in_walk_data.pos, edge_dirs[0])

    def next_positions(self, *in_walks):
        """applies next_pos to all entries of in_walks"""
        return tuple(self.next_pos(_) for _ in in_walks)

    def find_all_concave_corners(self):
        """returns all of the concave corners"""
        return {_ for _ in self.net if self.is_on_edge(_) and self.is_concave_corner(_)}


def _update_wrap_data(wrap_data, in_pos_a, inside_dir_a, in_pos_b, inside_dir_b):
    wrap_data[(in_pos_a, _negate_tuple(inside_dir_a))] = (in_pos_b, inside_dir_b)
    wrap_data[(in_pos_b, _negate_tuple(inside_dir_b))] = (in_pos_a, inside_dir_a)


def _update_wrap_data_at_regular_pos(wrap_data, edge_walker, in_pos_a, in_pos_b):
    _update_wrap_data(
        wrap_data,
        in_pos_a,
        edge_walker.get_dir_inside(in_pos_a),
        in_pos_b,
        edge_walker.get_dir_inside(in_pos_b),
    )


def _get_next_to_convex(edge_walker, walk_on_convex):
    tmp_dir = (
        walk_on_convex.dir
        if edge_walker.is_in(_make_shift(walk_on_convex.pos, walk_on_convex.dir))
        else _negate_tuple(walk_on_convex.dir)
    )

    return edge_walker.next_pos(WalkData(walk_on_convex.pos, tmp_dir))


def _update_wrap_data_at_convex_pos(wrap_data, edge_walker, walk_on_convex, in_pos):
    assert edge_walker.is_convex_corner(walk_on_convex.pos)
    next_to_convex = _get_next_to_convex(edge_walker, walk_on_convex)
    convex_insde_dir = edge_walker.get_dir_inside(next_to_convex.pos)
    _update_wrap_data(
        wrap_data,
        walk_on_convex.pos,
        convex_insde_dir,
        in_pos,
        edge_walker.get_dir_inside(in_pos),
    )


def _update_wrap_data_single_state(wrap_data, edge_walker, start_pos):
    start_dirs = edge_walker.get_edge_dirs(start_pos)
    assert len(start_dirs) == 2
    walk_a, walk_b = edge_walker.next_positions(
        *tuple(WalkData(start_pos, _) for _ in start_dirs)
    )
    while not (
        edge_walker.is_convex_corner(walk_a.pos)
        and edge_walker.is_convex_corner(walk_b.pos)
    ):
        if not edge_walker.is_convex_corner(
            walk_a.pos
        ) and not edge_walker.is_convex_corner(walk_b.pos):
            _update_wrap_data_at_regular_pos(
                wrap_data, edge_walker, walk_a.pos, walk_b.pos
            )
        elif edge_walker.is_convex_corner(walk_a.pos):
            _update_wrap_data_at_convex_pos(wrap_data, edge_walker, walk_a, walk_b.pos)
        else:
            assert edge_walker.is_convex_corner(walk_b.pos)
            _update_wrap_data_at_convex_pos(wrap_data, edge_walker, walk_b, walk_a.pos)
        walk_a, walk_b = edge_walker.next_positions(walk_a, walk_b)


def _compute_wrap_data(in_net):
    edge_walker = EdgeWalker(in_net)
    res = {}
    for start_pos in edge_walker.find_all_concave_corners():
        _update_wrap_data_single_state(res, edge_walker, start_pos)
    return res


class MoverCube(_Mover):
    """impelements a _Mover class in case of a walk on a net of a cube"""

    def __init__(self, map_data, start_pos):
        super().__init__(map_data, start_pos)
        self._wrap_data = _compute_wrap_data(self._map)

    def wrap_pos(self, in_pos, in_dir):
        """wraps the position as in part b"""
        assert in_pos in self._map
        return self._wrap_data[(in_pos, in_dir)]


def solve_b(in_str):
    """returns the solution for part_b"""
    return _solve(in_str, MoverCube)
