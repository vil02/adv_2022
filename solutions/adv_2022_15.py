"""solution of adv_2022_15"""

import re
import math
import sympy
import shapely


class SensorReading:
    """represents sensor reading"""

    def __init__(self, in_sensor, in_beacon):
        self._sensor = in_sensor
        self._beacon = in_beacon
        self._radius = manhattan_dist(self._sensor, self._beacon)

    def is_in_radius(self, in_pos):
        """checks if given position is covered area"""
        return manhattan_dist(in_pos, self.sensor) <= self._radius

    def __eq__(self, other):
        return self.sensor == other.sensor and self.beacon == other.beacon

    def get_covered_interval(self, in_row):
        """returns the interwal covered by this sensor in given row"""
        size_x = self._radius - abs(in_row - self.sensor[1])
        if size_x < 0:
            return sympy.S.EmptySet
        x_min = -size_x + self.sensor[0]
        x_max = size_x + self.sensor[0]
        assert self.is_in_radius((x_min, in_row))
        assert self.is_in_radius((x_max, in_row))
        assert not self.is_in_radius((x_min - 1, in_row))
        assert not self.is_in_radius((x_max + 1, in_row))
        return sympy.Interval(x_min, x_max)

    def get_covered_area(self):
        """returns area covered by this sensor"""
        pos_x, pos_y = self.sensor
        rad = self._radius
        res = shapely.Polygon(
            [
                (pos_x, pos_y - rad),
                (pos_x + rad, pos_y),
                (pos_x, pos_y + rad),
                (pos_x - rad, pos_y),
            ]
        )
        return res

    @property
    def sensor(self):
        """getter for _sensor"""
        return self._sensor

    @property
    def beacon(self):
        """getter for _beacon"""
        return self._beacon


def _proc_single_line(in_line):
    match = re.search(
        r"Sensor at x=(?P<sensor_x>-?\d*), y=(?P<sensor_y>-?\d*): "
        r"closest beacon is at x=(?P<beacon_x>-?\d*), y=(?P<beacon_y>-?\d*)",
        in_line,
    )

    def _as_int(group_name):
        return int(match.group(group_name))

    return SensorReading(
        _to_pos(_as_int("sensor_x"), _as_int("sensor_y")),
        _to_pos(_as_int("beacon_x"), _as_int("beacon_y")),
    )


def _to_pos(in_x, in_y):
    return (in_x, in_y)


def parse_input(in_str):
    """parses the input string into a list of SensorReadings"""
    return [_proc_single_line(_) for _ in in_str.splitlines()]


def manhattan_dist(pos_a, pos_b):
    """returns the manhattan distance"""
    return sum(abs(a - b) for a, b in zip(pos_a, pos_b))


def _get_covered(in_sensor_list, in_row):
    intervals = (_.get_covered_interval(in_row) for _ in in_sensor_list)
    return sympy.Union(*intervals)


def count_safe_in_row(in_sensor_list, in_row):
    """counts the pixels in given row, which do not contain a beacon"""
    covered = _get_covered(in_sensor_list, in_row).intersect(sympy.S.Integers)
    beacons_in_row = set(_.beacon for _ in in_sensor_list if _.beacon[1] == in_row)
    return len(covered) - len(beacons_in_row)


def solve_a(in_str):
    """returns the solution for part_a"""
    sensor_list = parse_input(in_str)
    return count_safe_in_row(sensor_list, 2000000)


def find_distress_beacon_fine(in_sensor_list, x_min, x_max, y_min, y_max):
    """find the uncovered pixel in specified area"""
    whole_row = sympy.Interval(x_min, x_max)
    res = None
    for cur_y in range(y_min, y_max + 1):
        covered = _get_covered(in_sensor_list, cur_y).intersect(whole_row)
        if covered.measure != x_max - x_min:
            uncovered = list(
                sympy.S.Integers.intersect(sympy.Complement(whole_row, covered))
            )
            assert len(uncovered) == 1
            res = uncovered[0], cur_y
            break
    return res


def find_distress_beacon(in_sensor_list, x_min, x_max, y_min, y_max):
    """calls find_distress_beacon_fine on smaller area"""
    search_space = shapely.geometry.box(x_min, y_min, x_max, y_max)
    covered = shapely.unary_union([_.get_covered_area() for _ in in_sensor_list])
    uncovered = search_space.difference(covered)
    fine_min_x = math.floor(uncovered.bounds[0])
    fine_min_y = math.floor(uncovered.bounds[1])
    fine_max_x = math.ceil(uncovered.bounds[2]) + 1
    fine_max_y = math.ceil(uncovered.bounds[3]) + 1
    return find_distress_beacon_fine(
        in_sensor_list, fine_min_x, fine_max_x, fine_min_y, fine_max_y
    )


def _search_limit():
    return 4000000


def tuning_frequency(in_x, in_y):
    """computes tuning frequency"""
    return _search_limit() * in_x + in_y


def solve_b(in_str):
    """returns the solution for part_b"""
    sensors = parse_input(in_str)
    search_size = (0, _search_limit())
    distress_beacon = find_distress_beacon(sensors, *search_size, *search_size)
    return tuning_frequency(*distress_beacon)
