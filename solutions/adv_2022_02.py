"""solution of adv_2022_02"""


def parse_input(in_str):
    """parses the input into a list of pairs/tuples"""

    def _parse_line(in_line_str):
        res = tuple(in_line_str.split())
        assert len(res) == 2
        return res

    return [_parse_line(_) for _ in in_str.splitlines()]


def _op_to_name(in_op):
    op_to_name = {"A": "R", "B": "P", "C": "S"}
    return op_to_name[in_op]


def _me_to_name(in_me):
    me_to_op = {"X": "A", "Y": "B", "Z": "C"}
    return _op_to_name(me_to_op[in_me])


def evaluate_single(in_data):
    """returns the score of single game as described in part A"""
    raw_op, raw_me = in_data
    op_name = _op_to_name(raw_op)
    me_name = _me_to_name(raw_me)

    used_item_score_dict = {"R": 1, "P": 2, "S": 3}

    game_score_dict = {
        ("R", "R"): 3,
        ("P", "P"): 3,
        ("S", "S"): 3,
        ("R", "P"): 6,
        ("P", "S"): 6,
        ("S", "R"): 6,
        ("R", "S"): 0,
        ("S", "P"): 0,
        ("P", "R"): 0,
    }

    return used_item_score_dict[me_name] + game_score_dict[(op_name, me_name)]


def solve_a(in_str):
    """returns the solution for part_a"""
    return sum(evaluate_single(_) for _ in parse_input(in_str))


def evaluate_single_b(in_data):
    """returns the score of single game as described in part B"""
    game_dict = {
        ("A", "X"): "Z",
        ("B", "Y"): "Y",
        ("C", "Z"): "X",
        ("A", "Y"): "X",
        ("A", "Z"): "Y",
        ("B", "Z"): "Z",
        ("B", "X"): "X",
        ("C", "X"): "Y",
        ("C", "Y"): "Z",
    }
    return evaluate_single((in_data[0], game_dict[in_data]))


def solve_b(in_str):
    """returns the solution for part_b"""
    return sum(evaluate_single_b(_) for _ in parse_input(in_str))
