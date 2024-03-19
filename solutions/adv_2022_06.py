"""solution of adv_2022_06"""

import collections


def make_histogram(in_str):
    """returns a dict representing a histogram of characters in in_str"""
    res = {}
    for _ in in_str:
        _increase_value(res, _)
    return res


def _decrease_value(histogram, in_key):
    histogram[in_key] -= 1
    if histogram[in_key] == 0:
        del histogram[in_key]


def _increase_value(histogram, in_key):
    histogram[in_key] = histogram.get(in_key, 0) + 1


class Block:
    """
    represents a block of text and allows to update in average constant time
    and check if the stored characters are all different in average constant time
    """

    def __init__(self, in_str):
        self._block_size = len(in_str)
        self._block = collections.deque(in_str)
        self._histogram = make_histogram(in_str)

    def _remove_char(self, in_char):
        _decrease_value(self._histogram, in_char)

    def _add_char(self, in_char):
        _increase_value(self._histogram, in_char)

    def update(self, new_char):
        """removes the oldest character and adds a new one"""
        first_char = self._block.popleft()
        self._block.append(new_char)
        if new_char != first_char:
            self._remove_char(first_char)
            self._add_char(new_char)

    def check(self):
        """returns true iff block consists of distinct characters"""
        return len(self._histogram) == self._block_size


def find_first_block_end(in_str, in_size):
    """returns the end of the first block of given size of different characters"""

    if in_size > len(in_str):
        raise ValueError("Input string is shorter than the block size.")
    cur_block = Block(in_str[:in_size])
    if cur_block.check():
        return in_size
    for cur_pos in range(in_size, len(in_str)):
        cur_block.update(in_str[cur_pos])
        if cur_block.check():
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
