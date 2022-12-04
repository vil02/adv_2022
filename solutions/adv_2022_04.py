"""solution of adv_2022_04"""


def parse_input(in_str):
    """parses the input into a list of pairs of interval"""

    def _is_interval(in_pair):
        return len(in_pair) == 2 and in_pair[0] <= in_pair[1]

    def _proc_interval_str(in_piece):
        res = tuple(int(_) for _ in in_piece.split("-"))
        assert _is_interval(res)
        return res

    def _proc_single_line(in_line):
        piece_list = in_line.split(",")
        assert len(piece_list) == 2
        return tuple(_proc_interval_str(_) for _ in piece_list)

    return [_proc_single_line(_) for _ in in_str.splitlines()]


def is_one_fully_contained(in_a, in_b):
    """checks if one of the intervals is fully contained in the other"""

    def _is_subset(in_x, in_y):
        return in_x[0] <= in_y[0] <= in_y[1] <= in_x[1]

    return _is_subset(in_a, in_b) or _is_subset(in_b, in_a)


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    return sum(1 for _ in data if is_one_fully_contained(*_))


def do_intersect(in_a, in_b):
    """checks if the intersection of the intervals in_a and in_b is non-empty"""

    def _is_left_end_in(in_x, in_y):
        return in_x[0] <= in_y[0] <= in_x[1]

    return (
        _is_left_end_in(in_a, in_b)
        or _is_left_end_in(in_b, in_a)
        or is_one_fully_contained(in_a, in_b)
    )


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    return sum(1 for _ in data if do_intersect(*_))
