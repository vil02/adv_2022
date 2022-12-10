"""solution of adv_2022_10"""

import collections

Addx = collections.namedtuple("Addx", ["value"])


def parse_input(in_str):
    """parses the input into..."""

    def _proc_single_line(in_line):
        if in_line == "noop":
            return in_line
        name, change = in_line.split(" ")
        assert name == "addx"
        return Addx(int(change))

    return [_proc_single_line(_) for _ in in_str.splitlines()]


class Computer:
    """represents the CPU"""

    def __init__(self):
        self._x_value = 1
        self._cycle = 0
        self._saved_cycles = [self._x_value]

    def _increase_cycle(self):
        self._cycle += 1
        self._saved_cycles.append(self._x_value)

    def run_single(self, in_cmd):
        """runns the single command"""
        if in_cmd == "noop":
            self._increase_cycle()
        else:
            assert isinstance(in_cmd, Addx)
            self._increase_cycle()
            self._increase_cycle()
            self._x_value += in_cmd.value

    def run(self, in_cmds):
        """runns all of the commands from in_cmds"""
        for _ in in_cmds:
            self.run_single(_)
        self._saved_cycles.append(self._x_value)

    @property
    def saved_cycles(self):
        """getter of _saved_cycles"""
        return self._saved_cycles


def signal_strength(cycle_num, x_value):
    """computes the signal strength"""
    return cycle_num * x_value


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    computer = Computer()
    computer.run(data)
    return sum(
        signal_strength(_, computer.saved_cycles[_])
        for _ in (20, 60, 100, 140, 180, 220)
    )


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    computer = Computer()
    computer.run(data)
    saved_cycles = computer.saved_cycles

    res = []
    cur_line = []
    pos = 0
    for _ in range(1, 241):
        if abs(saved_cycles[_] - pos) <= 1:
            cur_line.append("#")
        else:
            cur_line.append(".")
        pos += 1
        if _ % 40 == 0:
            pos = 0
            res.append("".join(cur_line))
            cur_line = []
    return res
