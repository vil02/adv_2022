"""solution of adv_2022_21"""

import collections

Operation = collections.namedtuple(
    "Operation", ["operation", "register_a", "register_b"]
)


def _proc_single_operation(in_str):
    if in_str.isnumeric():
        return int(in_str)
    register_a, operation, register_b = in_str.split(" ")
    assert operation in {"+", "-", "*", "/"}
    return Operation(operation=operation, register_a=register_a, register_b=register_b)


def parse_input(in_str):
    """parses the input into a dictionary, where values are ints or Operations"""
    res = {}
    for _ in in_str.splitlines():
        monkey_name, operation_str = _.split(": ")
        assert monkey_name not in res
        res[monkey_name] = _proc_single_operation(operation_str)
    return res


def evaluate(in_monkeys, monkey_name):
    """evaluates the current monkey computation"""
    cur_operation = in_monkeys[monkey_name]
    if isinstance(cur_operation, (int, float)):
        return in_monkeys[monkey_name]

    value_a = evaluate(in_monkeys, cur_operation.register_a)
    value_b = evaluate(in_monkeys, cur_operation.register_b)
    function_dict = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    return function_dict[cur_operation.operation](value_a, value_b)


def solve_a(in_str):
    """returns the solution for part_a"""
    monkeys = parse_input(in_str)
    return evaluate(monkeys, "root")


def _find_value(monkeys, humn_val):
    monkeys["humn"] = humn_val
    return evaluate(monkeys, "root")


def _find_interval(monkeys):
    cur_arg = 1
    while _find_value(monkeys, cur_arg) * _find_value(monkeys, -cur_arg) > 0:
        cur_arg *= 2
    return (-cur_arg, cur_arg)


def solve_b(in_str):
    """returns the solution for part_b"""
    monkeys = parse_input(in_str)
    old_root = monkeys["root"]
    monkeys["root"] = Operation("-", old_root.register_a, old_root.register_b)
    min_x, max_x = _find_interval(monkeys)
    mid_x = (min_x + max_x) // 2
    val_at_min = _find_value(monkeys, min_x)
    val_at_max = _find_value(monkeys, max_x)
    val_at_mid = _find_value(monkeys, mid_x)
    while val_at_mid != 0:
        if val_at_min * val_at_mid < 0:
            max_x = mid_x
            val_at_max = val_at_mid
        else:
            assert val_at_max * val_at_mid < 0
            min_x = mid_x
            val_at_min = val_at_mid
        mid_x = (min_x + max_x) // 2
        val_at_mid = _find_value(monkeys, mid_x)
    return mid_x
