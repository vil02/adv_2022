"""solution of adv_2022_14"""


def parse_input(in_str):
    """returns a tuple of tuples representing the wall corners"""

    def _proc_pair_str(in_str):
        x_pos, y_pos = in_str.split(",")
        return (int(x_pos), int(y_pos))

    def _proc_single_line(in_line):
        return tuple(_proc_pair_str(_) for _ in in_line.split(" -> "))

    return tuple(_proc_single_line(_) for _ in in_str.splitlines())


def _get_range(start, end):
    return range(min(start, end), max(start, end) + 1)


def _gen_pos_vertical(x_pos, y_start, y_end):
    for _ in _get_range(y_start, y_end):
        yield (x_pos, _)


def _gen_pos_horizontal(x_start, x_end, y_pos):
    for _ in _get_range(x_start, x_end):
        yield (_, y_pos)


def add_segment(walls, start_pos, end_pos):
    """adds single wall segment to walls"""
    if start_pos[0] == end_pos[0]:
        pos_generator = _gen_pos_vertical(start_pos[0], start_pos[1], end_pos[1])
    else:
        assert start_pos[1] == end_pos[1]
        pos_generator = _gen_pos_horizontal(start_pos[0], end_pos[0], start_pos[1])
    for _ in pos_generator:
        walls.add(_)


def add_line(walls, in_line):
    """adds a line of wall to walls"""
    for (cur_pos, cur_start) in enumerate(in_line[:-1]):
        add_segment(walls, cur_start, in_line[cur_pos + 1])


def generate_wall(in_lines):
    """returns all of the walls described by in_lines"""
    res = set()
    for _ in in_lines:
        add_line(res, _)
    return res


def y_limit(walls):
    """returns the y-limit"""
    return max(_[1] for _ in walls) + 1


def _move_down(in_pos):
    return in_pos[0], in_pos[1] + 1


def _move_left(in_pos):
    return in_pos[0] - 1, in_pos[1] + 1


def _move_right(in_pos):
    return in_pos[0] + 1, in_pos[1] + 1


class SandBox:
    """represents sand scene"""

    def __init__(self, source_pos, is_wall_fun, is_outside_fun):
        self._source_pos = source_pos
        self._is_wall = is_wall_fun
        self._is_outside = is_outside_fun
        self._sand = set()
        assert self._is_empty(self._source_pos)

    def _is_empty(self, pos):
        return pos not in self._sand and not self._is_wall(pos)

    def _next_pos(self, in_pos):
        for _ in (_move_down(in_pos), _move_left(in_pos), _move_right(in_pos)):
            if self._is_empty(_):
                return _
        return in_pos

    def _set_sand(self, in_pos):
        assert self._is_empty(in_pos)
        self._sand.add(in_pos)

    def add_single(self):
        """Returns False if it is not possible to add new sand."""
        cur_pos = self._source_pos
        if not self._is_empty(cur_pos):
            return False
        next_pos = self._next_pos(cur_pos)
        while next_pos != cur_pos:
            cur_pos = next_pos
            next_pos = self._next_pos(cur_pos)
            if self._is_outside(next_pos):
                return False
        self._set_sand(cur_pos)
        return True

    def count(self):
        """counts how many sand can be added to the current scene"""
        added = 0
        while self.add_single():
            added += 1
        return added


def solve_a(in_str):
    """returns the solution for part_a"""
    walls = generate_wall(parse_input(in_str))
    limit = y_limit(walls)
    sand_box = SandBox((500, 0), lambda pos: pos in walls, lambda pos: pos[1] > limit)
    return sand_box.count()


def solve_b(in_str):
    """returns the solution for part_b"""
    walls = generate_wall(parse_input(in_str))
    limit = y_limit(walls)
    sand_box = SandBox(
        (500, 0),
        lambda pos: pos in walls or pos[1] == limit + 1,
        lambda pos: pos[1] > limit + 1,
    )
    return sand_box.count()
