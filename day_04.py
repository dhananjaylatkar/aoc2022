from helper import get_input

inp = get_input(day=4)


def are_contained(r1, r2):
    return (
        r1[0] >= r2[0] and r1[0] <= r2[1] and r1[1] >= r2[0] and r1[1] <= r2[1]
    ) or (r2[0] >= r1[0] and r2[0] <= r1[1] and r2[1] >= r1[0] and r2[1] <= r1[1])


def are_overlaping(r1, r2):
    return (
        (r1[0] >= r2[0] and r1[0] <= r2[1])
        or (r1[1] >= r2[0] and r1[1] <= r2[1])
        or (r2[0] >= r1[0] and r2[0] <= r1[1])
        or (r2[1] >= r1[0] and r2[1] <= r1[1])
    )


def part_1_2():
    res1 = 0
    res2 = 0
    for spaces in inp:
        e1, e2 = spaces.split(",")
        r1 = [int(x) for x in e1.split("-")]
        r2 = [int(x) for x in e2.split("-")]
        if are_contained(r1, r2):
            res1 += 1
        if are_overlaping(r1, r2):
            res2 += 1
    return res1, res2


res1, res2 = part_1_2()
print(f"D04P1: {res1}")
print(f"D04P2: {res2}")
