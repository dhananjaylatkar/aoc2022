from helper import get_input
import copy

inp = get_input(day=5, no_strip=True)

box_stack = [[] for _ in range(9)]

# Create Box Stack
for i in range(8):
    row = inp[i].split(" ")
    row_simplified = []
    j = 0
    while j < len(row):
        if row[j] == "":
            j += 4
            row_simplified.append("")
        else:
            row_simplified.append(row[j][1])
            j += 1
    for i, box in enumerate(row_simplified):
        if box:
            box_stack[i].insert(0, box)


def part_1():
    _box_stack = copy.deepcopy(box_stack)
    for i in range(10, len(inp)):
        _, num, _, source, _, dest = inp[i].split()
        num, source, dest = [int(x) for x in [num, source, dest]]

        for _ in range(num):
            _box_stack[dest - 1].append(_box_stack[source - 1].pop())

    res = "".join([x[-1] for x in _box_stack])

    return res


def part_2():
    _box_stack = copy.deepcopy(box_stack)
    for i in range(10, len(inp)):
        _, num, _, source, _, dest = inp[i].split()
        num, source, dest = [int(x) for x in [num, source, dest]]

        _box_stack[dest - 1].extend(
            _box_stack[source - 1][len(_box_stack[source - 1]) - num :]
        )
        _box_stack[source - 1] = _box_stack[source - 1][
            : len(_box_stack[source - 1]) - num
        ]

    res = "".join([x[-1] for x in _box_stack])

    return res


print(f"D05P1: {part_1()}")
print(f"D05P2: {part_2()}")
