"""solution of adv_2022_09"""

import collections

Move = collections.namedtuple("Move", ["direction", "steps"])


def parse_input(in_str):
    """parses the input into..."""

    def _proc_single_line(in_line):
        move_dir, steps_str = in_line.split(" ")
        return Move(move_dir, int(steps_str))

    return [_proc_single_line(_) for _ in in_str.splitlines()]


def _shift_pos(in_pos, in_shift):
    return tuple(sum(_) for _ in zip(in_pos, in_shift))


def _get_direction(head_pos, tail_pos):
    return tuple(h - t for (h, t) in zip(head_pos, tail_pos))


def move_tail(head_pos, tail_pos):
    """returns the new tail position"""
    shift = _get_direction(head_pos, tail_pos)
    if shift == (0, 0) or all(abs(_) in {0, 1} for _ in shift):
        return tail_pos
    if 0 in shift:
        assert 2 in shift or -2 in shift
        return _shift_pos(tail_pos, tuple(_ // 2 for _ in shift))
    return _shift_pos(tail_pos, tuple(_ // abs(_) for _ in shift))


def _get_move_direction(in_move_direction):
    return {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}[in_move_direction]


class RopeSimulator:
    """represents a moving rope"""

    def __init__(self, rope_length=2):
        assert rope_length >= 2
        origin = (0, 0)
        self._length = rope_length
        self._knots = [origin for _ in range(rope_length)]
        self._visited_by_tail = {origin}

    def make_move(self, move):
        """makes a single move"""
        move_direction = _get_move_direction(move.direction)
        for _ in range(move.steps):
            self._knots[0] = _shift_pos(self._knots[0], move_direction)
            for _ in range(1, self._length):
                self._knots[_] = move_tail(self._knots[_ - 1], self._knots[_])
            self._visited_by_tail.add(self._knots[-1])

    def make_moves(self, moves):
        """makes all of the moves from the moves"""
        for _ in moves:
            self.make_move(_)

    @property
    def visited_by_tail(self):
        """returns the set of locations visited by the tail"""
        return self._visited_by_tail


def _run_simulation(in_str, rope_length):
    rope_simulator = RopeSimulator(rope_length)
    rope_simulator.make_moves(parse_input(in_str))
    return len(rope_simulator.visited_by_tail)


def solve_a(in_str):
    """returns the solution for part_a"""
    return _run_simulation(in_str, 2)


def solve_b(in_str):
    """returns the solution for part_b"""
    return _run_simulation(in_str, 10)
