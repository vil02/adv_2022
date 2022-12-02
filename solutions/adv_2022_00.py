"""solution of adv_2022_00"""


def solve_a(in_str):
    """returns the solution for part_a"""
    return sum(_ == "A" for _ in in_str)


def solve_b(in_str):
    """returns the solution for part_a"""
    return sum(_ == "B" for _ in in_str)
