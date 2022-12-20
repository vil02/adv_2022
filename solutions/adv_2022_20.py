"""solution of adv_2022_20"""


def parse_input(in_str):
    """parses the input into a tuple of ints"""
    return tuple(int(_) for _ in in_str.splitlines())


def mark_duplicates(in_data):
    """
    returns a tuple of unique pairs such that the first entries are values from in_data
    """
    res = []
    repeated = {}
    for _ in in_data:
        repeated[_] = repeated.get(_, -1) + 1
        res.append((_, repeated[_]))
    return tuple(res)


def _get_circular_index(in_list_len, in_index):
    return in_index % in_list_len


def _get_nth_index_after_element(in_list, in_element, in_shift):
    index = in_list.index(in_element)
    return _get_circular_index(len(in_list), index + in_shift)


def get_nth_after_zero(in_list, in_shift):
    """returns the element of in_list being in_shift positions behind zero"""
    return in_list[_get_nth_index_after_element(in_list, 0, in_shift)]


def make_mix(num_list, element):
    """makes single mixing step"""
    cur_num = element[0]
    if cur_num != 0:
        cur_start_ind = num_list.index(element)
        del num_list[cur_start_ind]
        new_ind = (cur_start_ind + cur_num) % len(num_list)
        num_list.insert(new_ind, element)


def _encrypt(in_nums, numer_of_rounds):
    nums = mark_duplicates(in_nums)
    tmp_nums = list(nums)
    for _ in range(numer_of_rounds):
        for element in nums:
            make_mix(tmp_nums, element)
    tmp_nums = [_[0] for _ in tmp_nums]

    return sum(get_nth_after_zero(tmp_nums, _) for _ in [1000, 2000, 3000])


def solve_a(in_str):
    """returns the solution for part_a"""
    nums = parse_input(in_str)
    return _encrypt(nums, 1)


def solve_b(in_str):
    """returns the solution for part_b"""
    nums = parse_input(in_str)
    nums = [_ * 811589153 for _ in nums]
    return _encrypt(nums, 10)
