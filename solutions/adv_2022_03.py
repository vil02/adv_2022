"""solution of adv_2022_03"""


def parse_input_a(in_str):
    """parses the input for part a"""

    def parse_single_line(in_line):
        assert len(in_line) % 2 == 0
        piece_a = in_line[0 : len(in_line) // 2]
        piece_b = in_line[len(in_line) // 2 :]
        assert len(piece_a) == len(piece_b)
        return (list(piece_a), list(piece_b))

    return [parse_single_line(_) for _ in in_str.splitlines()]


def get_priority(in_char):
    """returns the character priority"""
    if "A" <= in_char <= "Z":
        return ord(in_char) - 38
    if "a" <= in_char <= "z":
        return ord(in_char) - 96
    raise ValueError("Wrong input")


def solve_a(in_str):
    """returns the solution for part_a"""

    def proc_single_group(in_group):
        piece_a, piece_b = in_group
        common = list(set(piece_a).intersection(set(piece_b)))
        assert len(common) == 1
        return get_priority(common[0])

    data = parse_input_a(in_str)
    return sum(proc_single_group(_) for _ in data)


def parse_input_b(in_str, line_group_size):
    """parses the input for part b"""
    lines = in_str.splitlines()
    assert len(lines) % line_group_size == 0
    res = []
    for group_num in range(0, len(lines), line_group_size):
        res.append([list(lines[group_num + _]) for _ in range(line_group_size)])
    return res


def solve_b(in_str):
    """returns the solution for part_b"""

    def proc_single_group(in_group):
        common = list(set.intersection(*[set(_) for _ in in_group]))
        assert len(common) == 1
        return get_priority(common[0])

    data = parse_input_b(in_str, 3)
    return sum(proc_single_group(_) for _ in data)
