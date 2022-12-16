"""solution of adv_2022_15"""

import re


class SensorReading:
    def __init__(self, in_sensor, in_beacon):
        self._sensor = in_sensor
        self._beacon = in_beacon
        self._radius = manhattan_dist(self._sensor, self._beacon)

    def is_in_radius(self, in_pos):
        return manhattan_dist(in_pos, self.sensor) <= self._radius

    def __eq__(self, other):
        return self.sensor == other.sensor and other.beacon == other.beacon

    def get_covered_interval(self, in_row):
        size_x = self._radius - abs(in_row - self.sensor[1])
        if size_x < 0:
            return None
        x_min = -size_x + self.sensor[0]
        x_max = size_x + self.sensor[0]
        assert self.is_in_radius((x_min, in_row))
        assert self.is_in_radius((x_max, in_row))
        assert not self.is_in_radius((x_min - 1, in_row))
        assert not self.is_in_radius((x_max + 1, in_row))
        return (x_min, x_max)

    @property
    def sensor(self):
        return self._sensor

    @property
    def beacon(self):
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
    return sum(abs(a - b) for a, b in zip(pos_a, pos_b))


def count_safe_in_row(in_sensor_list, in_row):
    intervals = [
        _.get_covered_interval(in_row)
        for _ in in_sensor_list
        if _.get_covered_interval(in_row) is not None
    ]
    beacons_in_row = set(_.beacon for _ in in_sensor_list if _.beacon[1] == in_row)

    list_of_sets = [set(range(_[0], _[1] + 1)) for _ in intervals]
    return len(set.union(*list_of_sets)) - len(beacons_in_row)


def solve_a(in_str):
    """returns the solution for part_a"""
    sensor_list = parse_input(in_str)
    return count_safe_in_row(sensor_list, 2000000)


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    return 2 * sum(data)
