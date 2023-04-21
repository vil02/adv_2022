"""solution of adv_2022_05"""

import string
import re
import collections

Move = collections.namedtuple("Move", ["amount", "source", "target"])


def get_stack_number(in_col_num):
    """
    returns the stack number
    based on column number in the string represing the initial state
    """
    assert in_col_num % 4 == 1
    return (in_col_num - 1) // 4 + 1


def parse_input(in_str):
    """parses the input into..."""

    def _proc_initial_state_str(in_initial_state_str):
        res = {}
        for cur_line in in_initial_state_str.splitlines()[:-1]:
            for cur_col, cur_char in enumerate(cur_line):
                if cur_char in string.ascii_uppercase:
                    cur_stack_num = get_stack_number(cur_col)
                    res[cur_stack_num] = [cur_char] + res.get(cur_stack_num, [])
        return res

    def _proc_single_move_line(in_line):
        pattern = re.compile(
            r"move (?P<amount>\d*) from (?P<source>\d*) to (?P<target>\d*)"
        )
        match_data = pattern.match(in_line)
        return Move(
            int(match_data.group("amount")),
            int(match_data.group("source")),
            int(match_data.group("target")),
        )

    initial_state_str, moves_str = in_str.split("\n\n")
    initial_state = _proc_initial_state_str(initial_state_str)

    moves = [_proc_single_move_line(_) for _ in moves_str.splitlines()]
    return initial_state, moves


def make_move_a(state, in_move):
    """moves the containers as in part a"""
    for _ in range(in_move.amount):
        container = state[in_move.source].pop()
        state[in_move.target].append(container)


def make_moves(state, in_moves, in_move_fun):
    """makes all of the moves and update the state"""
    for _ in in_moves:
        in_move_fun(state, _)


def get_top_containers(in_state):
    """returns a string created by the characters representing the top containers"""
    return "".join(in_state[_][-1] for _ in sorted(in_state.keys()))


def solve_a(in_str):
    """returns the solution for part_a"""
    state, moves = parse_input(in_str)
    make_moves(state, moves, make_move_a)
    return get_top_containers(state)


def make_move_b(state, in_move):
    """moves the containers as in part b"""
    assert len(state[in_move.source]) >= in_move.amount
    containers = state[in_move.source][-in_move.amount :]
    del state[in_move.source][-in_move.amount :]
    state[in_move.target] += containers


def solve_b(in_str):
    """returns the solution for part_b"""
    state, moves = parse_input(in_str)
    make_moves(state, moves, make_move_b)
    return get_top_containers(state)
