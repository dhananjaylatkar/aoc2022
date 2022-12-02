from helper import get_input

inp = get_input(day=1)

curr_cal = 0
calories = []
for cal in inp:
    if cal:
        curr_cal += int(cal)
    else:
        calories.append(curr_cal)
        curr_cal = 0

calories = sorted(calories)

print(f"D01P1: {calories[-1]}")
print(f"D01P2: {calories[-1]+calories[-2]+calories[-3]}")
