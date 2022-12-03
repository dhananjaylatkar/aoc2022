from helper import get_input

inp = get_input(day=2)

"""
Rock defeats Scissors,
Scissors defeats Paper,
Paper defeats Rock.
"""

map = {"A": "X", "B": "Y", "C": "Z"}
points = {"X": 1, "Y": 2, "Z": 3}
win = {"X": "Z", "Z": "Y", "Y": "X"}
loss = dict((v, k) for k, v in win.items())
print_help = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}


def get_score(opp, pla):
    res = 0
    res += points[pla]
    if opp == pla:
        # Tie
        res += 3
    elif win[pla] == opp:
        # Win
        res += 6
    return res


def part_1():
    res = 0
    for turn in inp:
        opp, pla = turn.split()
        opp = map[opp]
        res += get_score(opp, pla)
    return res


def part_2():
    res = 0
    for turn in inp:
        opp, des = turn.split()
        opp = map[opp]
        pla = opp
        match des:
            case "X":
                # Loss
                pla = win[opp]
            case "Y":
                # TIe
                pla = opp
            case "Z":
                # Win
                pla = loss[opp]

        res += get_score(opp, pla)
    return res


print(f"D02P1: {part_1()}")
print(f"D02P2: {part_2()}")
