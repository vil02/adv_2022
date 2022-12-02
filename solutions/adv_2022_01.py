"""solution of adv_2022_01"""


def parse_input(in_str):
    """returns a list of lists of integers"""

    def proc_piece(in_piece_str):
        return [int(_) for _ in in_piece_str.splitlines()]

    piece_list = in_str.split("\n\n")
    return [proc_piece(_) for _ in piece_list]


def _count_sums(in_data):
    return [sum(_) for _ in in_data]


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    return max(_count_sums(data))


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    sorted_sums = sorted(_count_sums(data))
    assert len(sorted_sums) >= 3
    return sum(sorted_sums[-3:])
