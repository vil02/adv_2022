"""solution of adv_2022_07"""

import collections

_ROOT = "/"
_SEPARATOR = "|"


File = collections.namedtuple("File", ["name", "size"])


class Directory:
    """
    represents a directory containing:
    - list of files
    - (absolute) paths of its subdirectories
    """

    def __init__(self):
        self._files = []
        self._dirs = []

    def add_file(self, in_file):
        """adds a file"""
        self._files.append(in_file)

    def add_dir(self, in_dir):
        """adds a directory"""
        self._dirs.append(in_dir)

    def all_file_size(self):
        """
        returns the sum of all of the files stored in this directory
        (not in the subdirectories)
        """
        return sum(_.size for _ in self._files)

    @property
    def dirs(self):
        """getter for _dirs"""
        return self._dirs


def _get_dir_name_from_cd(in_cd_command):
    assert in_cd_command.startswith("$ cd ")
    pieces = in_cd_command.split(" ")
    assert len(pieces) == 3
    res = pieces[-1]
    assert _SEPARATOR not in res
    return res


def _change_dir(in_raw_dir, new_dir_name):
    if new_dir_name == _ROOT:
        return [new_dir_name]
    if new_dir_name == "..":
        return in_raw_dir[:-1]
    return in_raw_dir + [new_dir_name]


def _split_cmd_result_line(in_line):
    pieces = in_line.split(" ")
    assert len(pieces) == 2
    return pieces


def _is_file(in_line):
    return _split_cmd_result_line(in_line)[0].isnumeric()


def _parse_file_line(in_line):
    assert _is_file(in_line)
    pieces = _split_cmd_result_line(in_line)
    return File(pieces[1], int(pieces[0]))


def _is_dir(in_line):
    return _split_cmd_result_line(in_line)[0] == "dir"


def _parse_dir_line(cur_raw_dir, in_line):
    assert _is_dir(in_line)
    return _dir_to_str(cur_raw_dir + [_split_cmd_result_line(in_line)[1]])


def _dir_to_str(in_raw_dir):
    return _SEPARATOR.join(in_raw_dir) + _SEPARATOR


def parse_input(in_str):
    """parses the input into a list of Files"""
    res = {}
    cur_raw_dir = []
    for cur_line in in_str.splitlines():
        if cur_line.startswith("$ cd"):
            cur_raw_dir = _change_dir(cur_raw_dir, _get_dir_name_from_cd(cur_line))
        elif not cur_line.startswith("$"):
            if _dir_to_str(cur_raw_dir) not in res:
                res[_dir_to_str(cur_raw_dir)] = Directory()
            if _is_file(cur_line):
                res[_dir_to_str(cur_raw_dir)].add_file(_parse_file_line(cur_line))
            else:
                assert _is_dir(cur_line)
                res[_dir_to_str(cur_raw_dir)].add_dir(
                    _parse_dir_line(cur_raw_dir, cur_line)
                )
    return res


def get_dir_size(in_dir_path, in_dirs):
    """returns the total size of the directory"""
    cur_dir = in_dirs[in_dir_path]
    return cur_dir.all_file_size() + sum(get_dir_size(_, in_dirs) for _ in cur_dir.dirs)


def _get_dir_sizes(in_dirs):
    return {_: get_dir_size(_, in_dirs) for _ in in_dirs}


def _get_sizes_form_str(in_str):
    return _get_dir_sizes(parse_input(in_str))


def solve_a(in_str):
    """returns the solution for part_a"""
    sizes = _get_sizes_form_str(in_str)
    return sum(_ for _ in sizes.values() if _ <= 100000)


def solve_b(in_str):
    """returns the solution for part_b"""
    sizes = _get_sizes_form_str(in_str)
    used_space = sizes[_ROOT + _SEPARATOR]
    total_space = 70000000
    assert used_space <= total_space
    needed_space = 30000000
    to_be_deleted = used_space - (total_space - needed_space)
    assert to_be_deleted >= 0
    return min(_ for _ in sizes.values() if _ >= to_be_deleted)
