from helper import get_input
from pprint import pprint
import copy
import math

inp = get_input(day=11)

MONKEYS = {}

for i in range(0, len(inp), 7):
    monkey = int(inp[i].split(" ")[-1][:-1])
    items = [int(x) for x in inp[i + 1].split(":")[-1].split(",")]
    operation = inp[i + 2].split("=")[-1].split()

    test = [
        int(inp[i + 3].split()[-1]),
        int(inp[i + 4].split()[-1]),
        int(inp[i + 5].split()[-1]),
    ]

    MONKEYS[monkey] = {
        "items": items,
        "operation": operation,
        "test": test,
        "inspections": 0,
    }


# pprint(monkeys)


def do_operation(item, operation):
    operation = [item if x == "old" else x for x in operation]
    operation[-1] = int(operation[-1])
    v1, op, v2 = operation
    res = 0
    match op:
        case "+":
            res = v1 + v2
        case "-":
            res = v1 - v2
        case "*":
            res = v1 * v2
        case "/":
            res = v1 / v2
    # print(operation, res)
    return res


def do_test(worry, test):
    """
    Return which monkey to pass the item
    """

    div, t, f = test

    if worry % div == 0:
        return t
    return f


def part_1():
    monkeys = copy.deepcopy(MONKEYS)
    for _ in range(20):
        for monkey, ops in monkeys.items():
            for item in ops["items"]:
                new_worry = do_operation(item, ops["operation"]) // 3
                new_monkey = do_test(new_worry, ops["test"])
                monkeys[new_monkey]["items"].append(new_worry)
                ops["inspections"] += 1
            ops["items"] = []

    # for monkey, ops in monkeys.items():
    #     print("Monkey", monkey, ops["items"])

    x, y, *_ = sorted([x["inspections"] for x in monkeys.values()], reverse=True)
    return x * y


def part_2():
    monkeys = copy.deepcopy(MONKEYS)
    mod_lcm = math.lcm(*[x["test"][0] for x in monkeys.values()])

    for _ in range(10000):
        for monkey, ops in monkeys.items():
            for item in ops["items"]:
                new_worry = do_operation(item, ops["operation"]) % mod_lcm
                new_monkey = do_test(new_worry, ops["test"])
                monkeys[new_monkey]["items"].append(new_worry)
                ops["inspections"] += 1
            ops["items"] = []

    # for monkey, ops in monkeys.items():
    #     print("Monkey", monkey, ops["items"])

    x, y, *_ = sorted([x["inspections"] for x in monkeys.values()], reverse=True)
    return x * y


print(f"D11P1: {part_1()}")
print(f"D11P2: {part_2()}")
