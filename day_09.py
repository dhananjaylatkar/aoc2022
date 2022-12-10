from helper import get_input

inp = get_input(day=9)


def part_1_2():
    dirs = {"U": 1j, "D": -1j, "L": -1, "R": 1}
    sign = lambda a: (a > 0) - (a < 0)
    rope, s1, s2 = [0] * 10, {0}, {0}

    for move in inp:
        d, s = move.split()

        for _ in range(int(s)):
            rope[0] += dirs[d]

            for i in range(1, len(rope)):
                if abs(diff := rope[i - 1] - rope[i]) >= 2:
                    rope[i] += complex(sign(diff.real), sign(diff.imag))

            s1.add(rope[1])
            s2.add(rope[-1])
    return len(s1), len(s2)


p1, p2 = part_1_2()
print(f"D09P1: {p1}")
print(f"D09P2: {p2}")
