"""solution of adv_2022_06"""

import collections


def parse_input(in_str):
    """parses the input into..."""

    def _proc_single_line(in_line):
        return len(in_line)

    return [_proc_single_line(_) for _ in in_str.splitlines()]


def find_first_block_end(in_str, in_size):
    """returns the end of the first block of given size of different characters"""

    def _check_block(in_block):
        return len(set(list(in_block))) == in_size

    if in_size > len(in_str):
        raise ValueError("Input string is shorter than the block size.")

    cur_block = collections.deque(in_str[:in_size], maxlen=in_size)
    if _check_block(cur_block):
        return in_size

    for cur_pos in range(in_size, len(in_str)):
        cur_block.append(in_str[cur_pos])
        if _check_block(cur_block):
            return cur_pos + 1
    raise ValueError(
        f"Could not find a block of distinct characters of size {in_size}."
    )


def solve_a(in_str):
    """returns the solution for part_a"""
    return find_first_block_end(in_str, 4)


def solve_b(in_str):
    """returns the solution for part_b"""
    return find_first_block_end(in_str, 14)
