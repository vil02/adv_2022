"""solution of adv_2022_07"""

import collections

_ROOT = "/"
_SEPARATOR = "|"


def _get_dir_name_from_cd(in_cd_command):
    assert in_cd_command.startswith("$ cd ")
    pieces = in_cd_command.split(" ")
    assert len(pieces) == 3
    res = pieces[-1]
    assert _SEPARATOR not in res
    return res


def _change_dir(in_dir, new_dir):
    if new_dir == _ROOT:
        return [new_dir]
    if new_dir == "..":
        return in_dir[:-1]
    return in_dir + [new_dir]


def _is_file(in_line):
    pieces = in_line.split(" ")
    assert len(pieces) == 2
    return pieces[0].isnumeric()


def _parse_file_line(cur_dir, in_line):
    assert _is_file(in_line)
    pieces = in_line.split(" ")
    file = collections.namedtuple("File", ["dir", "name", "size"])
    return file(cur_dir, pieces[1], int(pieces[0]))


def _dir_to_str(in_dir):
    return _SEPARATOR.join(in_dir) + _SEPARATOR


def parse_input(in_str):
    """parses the input into a list of Files"""
    res = []
    cur_dir = None
    for cur_line in in_str.splitlines():
        if cur_line.startswith("$ cd"):
            cur_dir = _change_dir(cur_dir, _get_dir_name_from_cd(cur_line))
        elif not cur_line.startswith("$") and _is_file(cur_line):
            res.append(_parse_file_line(_dir_to_str(cur_dir), cur_line))
    return res


def _is_subdir(dir_a, dir_b):
    """returns true if dir_b is a subdir of dir_a"""
    return dir_b.startswith(dir_a)


def _gen_all_superdirs(in_dir):
    raw_dir = in_dir[:-1].split(_SEPARATOR)
    for cur_len in range(1, len(raw_dir) + 1):
        yield _dir_to_str(raw_dir[:cur_len])


def _get_all_dirs(in_file_list):
    dirs = [_.dir for _ in in_file_list]
    res = []
    for cur_dir in dirs:
        res.append(cur_dir)
        for _ in _gen_all_superdirs(cur_dir):
            res.append(_)
    return set(res)


def _get_dir_size(in_dir, in_files):
    return sum(_.size for _ in in_files if _is_subdir(in_dir, _.dir))


def _get_dir_sizes(in_files):
    dirs = _get_all_dirs(in_files)
    return {_: _get_dir_size(_, in_files) for _ in dirs}


def _get_dir_sizes_from_str(in_str):
    files = parse_input(in_str)
    return _get_dir_sizes(files)


def solve_a(in_str):
    """returns the solution for part_a"""
    sizes = _get_dir_sizes_from_str(in_str)
    return sum(_ for _ in sizes.values() if _ <= 100000)


def solve_b(in_str):
    """returns the solution for part_b"""
    sizes = _get_dir_sizes_from_str(in_str)
    used_space = sizes[_ROOT + _SEPARATOR]
    total_space = 70000000
    assert used_space <= total_space
    needed_space = 30000000
    to_be_deleted = used_space - (total_space - needed_space)
    assert to_be_deleted >= 0
    return min(_ for _ in sizes.values() if _ >= to_be_deleted)
