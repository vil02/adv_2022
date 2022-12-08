"""solution of adv_2022_08"""


def parse_input(in_str):
    """parses the input into..."""

    def _proc_single_line(in_line):
        return tuple(int(_) for _ in in_line)

    return tuple(_proc_single_line(_) for _ in in_str.splitlines())


def _is_in_range(height_data, in_pos):
    x_pos, y_pos = in_pos
    return 0 <= y_pos < len(height_data) and 0 <= x_pos < len(height_data[y_pos])


def get_height(height_data, in_pos):
    """
    Returns the height at given positon.
    If position is outside the range, it returns -1.
    """
    if not _is_in_range(height_data, in_pos):
        return -1
    x_pos, y_pos = in_pos
    return height_data[y_pos][x_pos]


def _shift_pos(in_pos, in_shift):
    return tuple(a + b for (a, b) in zip(in_pos, in_shift))


def _shift_pos_back(in_pos, in_shift):
    return _shift_pos(in_pos, tuple(-_ for _ in in_shift))


def compute_is_visible(height_data):
    """
    returns a list of boolen lists descibing if given tree is visible from outside
    """
    res = [[False for _ in cur_row] for cur_row in height_data]

    def _set_to_visible(in_pos):
        x_pos, y_pos = in_pos
        res[y_pos][x_pos] = True

    def _proc_ray(start_pos, direction):
        max_height = get_height(height_data, _shift_pos_back(start_pos, direction))
        cur_pos = start_pos
        while _is_in_range(height_data, cur_pos):
            cur_height = get_height(height_data, cur_pos)
            if cur_height > max_height:
                _set_to_visible(cur_pos)
                max_height = cur_height
            cur_pos = _shift_pos(cur_pos, direction)

    for start_x in range(len(height_data[0])):
        _proc_ray((start_x, 0), (0, 1))
    for start_x in range(len(height_data[-1])):
        _proc_ray((start_x, len(height_data[-1]) - 1), (0, -1))

    for (start_y, row) in enumerate(height_data):
        _proc_ray((0, start_y), (1, 0))
        _proc_ray((len(row) - 1, start_y), (-1, 0))

    return res


def solve_a(in_str):
    """returns the solution for part_a"""
    height_data = parse_input(in_str)
    is_visible = compute_is_visible(height_data)
    return sum(sum(1 for _ in cur_row if _) for cur_row in is_visible)


def compute_scenic_score(height_data, in_pos):
    """returns the scenic score"""
    start_height = get_height(height_data, in_pos)

    def _proc_ray(direction):
        cur_pos = _shift_pos(in_pos, direction)
        if not _is_in_range(height_data, cur_pos):
            return 0
        cur_score = 1
        while (
            _is_in_range(height_data, _shift_pos(cur_pos, direction))
            and get_height(height_data, cur_pos) < start_height
        ):
            cur_pos = _shift_pos(cur_pos, direction)
            cur_score += 1
        return cur_score

    return (
        _proc_ray((0, 1)) * _proc_ray((0, -1)) * _proc_ray((1, 0)) * _proc_ray((-1, 0))
    )


def solve_b(in_str):
    """returns the solution for part_b"""
    height_data = parse_input(in_str)
    res = -1
    for y_pos, row in enumerate(height_data):
        for x_pos in range(len(row)):
            res = max(res, compute_scenic_score(height_data, (x_pos, y_pos)))
    return res
