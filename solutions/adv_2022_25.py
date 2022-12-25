"""solution of adv_2022_25"""


def _snafu_to_decimal_single_digit(in_snafu_digit):
    return {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}[in_snafu_digit]


def snafu_to_decimal(in_snafu):
    """converts a snafu number to decimal int"""
    res = 0
    multip = 5
    for _ in in_snafu:
        res *= multip
        res += _snafu_to_decimal_single_digit(_)
    return res


def decimal_to_snafu(in_decimal):
    """converts a decmal int into snafu"""
    carry_over = 0
    res = []
    cur_val = in_decimal
    base = 5
    while cur_val:
        cur_digit = cur_val % base
        cur_val //= base

        cur_digit += carry_over
        carry_over = 0
        if cur_digit in {3, 4}:
            cur_digit = "=" if cur_digit == 3 else "-"
            carry_over = 2 if cur_digit == 3 else 1
        elif cur_digit == 5:
            cur_digit = "0"
            carry_over = 1
        res.append(str(cur_digit))

    if carry_over:
        res.append(str(carry_over))
    return "".join(reversed(res))


def solve_a(in_str):
    """returns the sum of the inpus snafu numbers as snafu number"""
    res_dec = sum(snafu_to_decimal(_) for _ in in_str.splitlines())
    return decimal_to_snafu(res_dec)
