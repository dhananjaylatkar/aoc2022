from helper import get_input
import json
from functools import cmp_to_key

inp = get_input(day=13)


def is_inorder(a, b):
    match a, b:
        case int(), list():
            return is_inorder([a], b)
        case list(), int():
            return is_inorder(a, [b])
        case int(), int():
            return a - b
        case list(), list():
            for i, j in zip(a, b):
                if (r := is_inorder(i, j)) != 0:
                    return r
            return is_inorder(len(a), len(b))


PACKETS = [[[2]], [[6]]]


def part_1():
    res = 0
    pair = 1
    for i in range(0, len(inp), 3):
        a = json.loads(inp[i])
        b = json.loads(inp[i + 1])
        PACKETS.append(a)
        PACKETS.append(b)
        if is_inorder(a, b) <= 0:
            res += pair
        pair += 1
    return res


def part_2():
    two = None
    six = None
    global PACKETS
    PACKETS = sorted(PACKETS, key=cmp_to_key(is_inorder))
    for i, pkt in enumerate(PACKETS, start=1):
        if pkt == [[2]]:
            two = i
        elif pkt == [[6]]:
            six = i
    return two * six


print(f"D13P1: {part_1()}")
print(f"D13P2: {part_2()}")
