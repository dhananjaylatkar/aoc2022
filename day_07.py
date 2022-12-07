from helper import get_input

inp = get_input(day=7)


class File:
    def __init__(self, name, size, parent, is_dir):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        if self.is_dir:
            self.sub = {}


def print_dirs(root):
    if root.parent:
        print(root.name, root.size, root.parent.name)
    else:
        print(root.name, root.size, root.parent)

    for _, s in root.sub.items():
        if s.is_dir:
            print_dirs(s)
        else:
            print(s.name, s.size, s.parent.name)


root = File("/", 0, None, True)  # root directory


def create_dir_graph():
    curr = None
    for f in inp:
        if f.startswith("$ cd"):
            curr_dir = f.split()[-1]
            if curr_dir == "..":
                curr = curr.parent
            elif curr_dir == "/":
                curr = root
            else:
                curr = curr.sub[curr_dir]
        elif f.startswith("$ ls"):
            pass
        elif f.startswith("dir"):
            dir_name = f.split()[-1]
            curr.sub[dir_name] = File(dir_name, 0, curr, True)
        else:
            si, fi = f.split()
            curr.sub[fi] = File(fi, int(si), curr, False)


def update_dir_sizes(root):
    if root.is_dir:
        for _, f in root.sub.items():
            root.size += update_dir_sizes(f)
    return root.size


def part_1(root):
    res = 0

    def dfs(_root):
        nonlocal res
        if not _root.is_dir:
            return
        if _root.is_dir and _root.size <= 100000:
            res += _root.size
        for _, f in _root.sub.items():
            dfs(f)

    dfs(root)
    return res


def part_2(root):
    res = 70000000  # Some big value
    FS_SIZE = 70000000
    FREE_SPACE = FS_SIZE - root.size
    REQ_FREE_SPACE = 30000000
    SPACE_TO_FREE = REQ_FREE_SPACE - FREE_SPACE

    def dfs(_root):
        nonlocal res
        nonlocal SPACE_TO_FREE
        if not _root.is_dir:
            return
        if _root.is_dir and _root.size >= SPACE_TO_FREE:
            res = min(res, _root.size)
        for _, f in _root.sub.items():
            dfs(f)

    dfs(root)
    return res


create_dir_graph()
update_dir_sizes(root)
# print_dirs(root)
print(f"D07P1: {part_1(root)}")
print(f"D07P2: {part_2(root)}")
