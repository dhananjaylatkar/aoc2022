from helper import get_input_split

inp = get_input_split(day=10)


def part_1_2():
    cycles = set([20, 60, 100, 140, 180, 220])
    X = 1
    res = 0
    CRT = ["."] * 40 * 6
    curr = 0
    for cycle, op in enumerate(inp, start=1):
        if cycle in cycles:
            res += cycle * X
        if curr % 40 in (X - 1, X, X + 1):
            CRT[curr] = "#"
        curr += 1
        if op[-1].isdigit():
            X += int(op)

    print(f"D10P1: {res}")

    for i in range(0, 40 * 6, 40):
        print("D10P2:", "".join(CRT[i : i + 40]))


part_1_2()
