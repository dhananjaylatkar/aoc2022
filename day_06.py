from helper import get_input

inp = get_input(day=6)[0]


def get_unique_idx(msg_size):
    for i in range(0, len(inp)):
        s = set([x for x in inp[i : i + msg_size]])
        if len(s) == msg_size:
            return i + msg_size


def part_1():
    return get_unique_idx(4)


def part_2():
    return get_unique_idx(14)


print(f"D06P1: {part_1()}")
print(f"D06P2: {part_2()}")
