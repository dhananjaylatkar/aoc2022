from helper import get_input

inp = get_input(day=3)


def get_priority(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26


def part_1():
    res = 0
    for sack in inp:
        n = len(sack) // 2
        s1 = set([x for x in sack[:n]])
        s2 = set([x for x in sack[n:]])
        common = s1.intersection(s2)

        for c in common:
            res += get_priority(c)

    return res


def part_2():
    res = 0
    for i in range(0, len(inp), 3):
        s1 = set([x for x in inp[i]])
        s2 = set([x for x in inp[i + 1]])
        s3 = set([x for x in inp[i + 2]])
        badge = s1.intersection(s2).intersection(s3)
        res += get_priority(list(badge)[0])
    return res


print(f"D03P1: {part_1()}")
print(f"D03P2: {part_2()}")
