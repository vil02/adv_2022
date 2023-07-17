"""tests of adv_2022_07"""

import collections
import pytest
import general_utils as gu
import solutions.adv_2022_07 as sol

_DAY_NUM = 7


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_small_r():
    return gu.read_input(_DAY_NUM, "small_r")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


_EXAMPLE_DATA = sol.parse_input(_data_small())

Sizes = collections.namedtuple("Sizes", ["simple_size", "total_size"])
_EXPECTED_SIZES = {
    "/|": Sizes(14848514 + 8504156, 48381165),
    "/|a|": Sizes(29116 + 2557 + 62596, 29116 + 2557 + 62596 + 584),
    "/|a|e|": Sizes(584, 584),
    "/|d|": Sizes(
        4060174 + 8033020 + 5626152 + 7214296, 4060174 + 8033020 + 5626152 + 7214296
    ),
}


@pytest.mark.parametrize(
    "dir_path, expected",
    [(dir_path, size.simple_size) for (dir_path, size) in _EXPECTED_SIZES.items()],
)
def test_all_file_size(dir_path, expected):
    """tests Dictionary.all_file_size agains example data"""
    assert _EXAMPLE_DATA[dir_path].all_file_size() == expected


@pytest.mark.parametrize(
    "dir_path, expected",
    [(dir_path, size.total_size) for (dir_path, size) in _EXPECTED_SIZES.items()],
)
def test_get_dir_size(dir_path, expected):
    """tests get_dir_size agains example data"""
    assert sol.get_dir_size(dir_path, _EXAMPLE_DATA) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 95437, id="small"),
        pytest.param(_data_small_r(), 99999, id="small_r"),
        pytest.param(_data_p(), 1453349, id="p"),
        pytest.param(_data_s(), 1501149, id="s"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 24933642, id="small"),
        pytest.param(_data_small_r(), 50099999, id="small_r"),
        pytest.param(_data_p(), 2948823, id="p"),
        pytest.param(_data_s(), 10096985, id="s"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
