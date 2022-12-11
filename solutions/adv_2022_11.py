"""solution of adv_2022_11"""

import collections
import math


def get_multiply_by(in_multip):
    """returns a function: x -> x*in_change"""

    def inner(in_val):
        return in_val * in_multip

    return inner


def get_increase_by(in_change):
    """returns a function: x -> x + in_change"""

    def inner(in_val):
        return in_val + in_change

    return inner


def get_make_square():
    """returns a function: x -> x*x"""

    def inner(in_val):
        return in_val * in_val

    return inner


Transfer = collections.namedtuple("Transfer", ["target", "item"])


class ItemManipulatorA:
    """represents an item/worry level change as in part a"""

    def __init__(self, in_operation):
        self._operation = in_operation

    def __call__(self, in_val):
        return self._operation(in_val) // 3

    def __eq__(self, other):
        return self._operation.__code__.co_code == other._operation.__code__.co_code


class ItemManipulatorB:
    """represents an item/worry level change as in part b"""

    def __init__(self, in_operation, in_mod_val):
        self._operation = in_operation
        self._mod_val = in_mod_val

    def __call__(self, in_val):
        return self._operation(in_val) % self._mod_val

    def __eq__(self, other):
        return (
            self._operation.__code__.co_code == other._operation.__code__.co_code
            and self._mod_val == other._mod_val
        )


class Thrower:
    """allows to throw an item to another monkey"""

    def __init__(self, in_divisor, in_target_if_true, in_target_if_false):
        self._divisor = in_divisor
        self._target_dict = {True: in_target_if_true, False: in_target_if_false}

    def __call__(self, in_val):
        return Transfer(self._target_dict[in_val % self._divisor == 0], in_val)

    def __eq__(self, other):
        return (
            self._divisor == other._divisor and self._target_dict == other._target_dict
        )


class Monkey:
    """represents a monkey"""

    def __init__(self, in_items, in_manipulator, in_thrower):
        self._items = in_items
        self._manipulator = in_manipulator
        self._thrower = in_thrower
        self._inspected_items = 0

    def __eq__(self, other):
        return (
            self._items == other._items
            and self._manipulator == other._manipulator
            and self._thrower == other._thrower
        )

    @property
    def items(self):
        """getter for _items"""
        return self._items

    @property
    def inspected_items(self):
        """getter for _inspected_items"""
        return self._inspected_items

    def add_item(self, in_item):
        """adds a new item"""
        self._items.append(in_item)

    def __call__(self):
        res = []
        while self._items:
            cur_item = self.items.pop(0)
            cur_item = self._manipulator(cur_item)
            res.append(self._thrower(cur_item))
            self._inspected_items += 1
        return res


def parse_input(in_str, get_manipulator):
    """parses the input into..."""

    def _remove_prefix(in_prefix, in_str):
        assert in_str.startswith(in_prefix)
        return in_str[len(in_prefix) :]

    def _get_trailling_int(in_prefix, in_str):
        return int(_remove_prefix(in_prefix, in_str))

    def _get_items(in_str):
        return [
            int(_) for _ in _remove_prefix("  Starting items: ", in_str).split(", ")
        ]

    def _get_divisor(in_str):
        return _get_trailling_int("  Test: divisible by ", in_str)

    def _get_operation(in_str):
        operation_str = _remove_prefix("  Operation: new = ", in_str)
        _, operation, arg_2 = operation_str.split(" ")
        if arg_2 == "old":
            assert operation == "*"
            return get_make_square()
        arg_2 = int(arg_2)
        if operation == "*":
            return get_multiply_by(arg_2)
        assert operation == "+"
        return get_increase_by(arg_2)

    def _get_target_monkey_if_true(in_str):
        return _get_trailling_int("    If true: throw to monkey ", in_str)

    def _get_target_monkey_if_false(in_str):
        return _get_trailling_int("    If false: throw to monkey ", in_str)

    def _proc_single_block(in_num, in_block):
        lines = in_block.splitlines()
        assert lines[0] == f"Monkey {in_num}:"
        assert len(lines) == 6
        items = _get_items(lines[1])
        operation = _get_operation(lines[2])
        divisor = _get_divisor(lines[3])
        target_if_true = _get_target_monkey_if_true(lines[4])
        target_if_false = _get_target_monkey_if_false(lines[5])
        return (
            Monkey(
                items,
                get_manipulator(operation),
                Thrower(divisor, target_if_true, target_if_false),
            ),
            divisor,
        )

    monkeys, divisors = zip(
        *[
            _proc_single_block(num, block)
            for num, block in enumerate(in_str.split("\n\n"))
        ]
    )
    return monkeys, math.lcm(*divisors)


def make_round(monkeys):
    """makes a single round"""
    for _ in monkeys:
        transfers = _()
        for _ in transfers:
            monkeys[_.target].add_item(_.item)


def make_rounds(monkeys, number_of_rounds):
    """makes a specifed number of rounds"""
    for _ in range(number_of_rounds):
        make_round(monkeys)


def solve_a(in_str):
    """returns the solution for part_a"""
    monkeys, _ = parse_input(in_str, ItemManipulatorA)
    make_rounds(monkeys, 20)
    nums = sorted([_.inspected_items for _ in monkeys])
    return nums[-1] * nums[-2]


def solve_b(in_str):
    """returns the solution for part_b"""
    _, mod_val = parse_input(in_str, ItemManipulatorA)

    def get_manipulator_b(in_operation):
        return ItemManipulatorB(in_operation, mod_val)

    monkeys, _ = parse_input(in_str, get_manipulator_b)

    make_rounds(monkeys, 10000)
    nums = sorted([_.inspected_items for _ in monkeys])
    return nums[-1] * nums[-2]
