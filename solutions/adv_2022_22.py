"""solution of adv_2022_22"""

import collections
import string


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


def _make_shift(in_pos, in_shift):
    return tuple(p + s for p, s in zip(in_pos, in_shift))


class _Mover:
    def __init__(self, map_data, start_pos):
        self._map = map_data
        self._cur_pos = start_pos
        self._cur_dir = (1, 0)

    def wrap_pos(self, in_pos, in_dir):
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
        wraped_pos = self.wrap_pos(self.cur_pos, self.cur_dir)
        if self._is_empty(wraped_pos):
            self._cur_pos = wraped_pos

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


class MoverA(_Mover):
    def __init__(self, map_data, start_pos):
        super().__init__(map_data, start_pos)
        self._wraps = {}

    def wrap_pos(self, in_pos, in_dir):
        """wraps the position as in part a"""
        assert in_pos in self._map
        if (in_pos, in_dir) in self._wraps:
            return self._wraps[(in_pos, in_dir)]
        search_dir = tuple(-_ for _ in in_dir)
        tmp_pos = in_pos
        while tmp_pos in self._map:
            tmp_pos = _make_shift(tmp_pos, search_dir)
        res = _make_shift(tmp_pos, in_dir)
        self._wraps[(in_pos, in_dir)] = res
        return res


def _facing(in_dir):
    return {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[in_dir]


def get_pwd(in_pos, in_dir):
    """returns the password of given positon/direction"""
    return 1000 * in_pos[1] + 4 * in_pos[0] + _facing(in_dir)


def solve_a(in_str):
    """returns the solution for part_a"""
    parse_res = parse_input(in_str)
    mover = MoverA(parse_res.map, parse_res.start_pos)
    mover.make_moves(parse_res.moves)
    return get_pwd(mover.cur_pos, mover.cur_dir)


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    return 2 * sum(data)
