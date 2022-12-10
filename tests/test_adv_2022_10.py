"""tests of adv_2022_10"""

import pytest
import general_utils as gu
import solutions.adv_2022_10 as sol

_DAY_NUM = 10


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_bigger():
    return gu.read_input(_DAY_NUM, "bigger")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def test_run():
    """tests run method of the Computer with small example data"""
    cmds = sol.parse_input(_data_small())
    computer = sol.Computer()
    computer.run(cmds)
    assert computer.saved_cycles == [1, 1, 1, 1, 4, 4, -1]


@pytest.mark.parametrize(
    "input_cycle,input_x,expected",
    [
        (20, 21, 420),
        (60, 19, 1140),
        (100, 18, 1800),
        (140, 21, 2940),
        (180, 16, 2880),
        (220, 18, 3960),
    ],
)
def test_signal_strength(input_cycle, input_x, expected):
    """tests signal_strength"""
    assert sol.signal_strength(input_cycle, input_x) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_bigger(), 13140, id="bigger"),
        pytest.param(_data_p(), 17020, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


_EXPECTED_BIGGER = [
    """##..##..##..##..##..##..##..##..##..##..""",
    """###...###...###...###...###...###...###.""",
    """####....####....####....####....####....""",
    """#####.....#####.....#####.....#####.....""",
    """######......######......######......####""",
    """#######.......#######.......#######.....""",
]

_EXPECTED_P = [
    """###..#....####.####.####.#.....##..####.""",
    """#..#.#....#.......#.#....#....#..#.#....""",
    """#..#.#....###....#..###..#....#....###..""",
    """###..#....#.....#...#....#....#.##.#....""",
    """#.#..#....#....#....#....#....#..#.#....""",
    """#..#.####.####.####.#....####..###.####.""",
]


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_bigger(), _EXPECTED_BIGGER, id="bigger"),
        pytest.param(_data_p(), _EXPECTED_P, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
