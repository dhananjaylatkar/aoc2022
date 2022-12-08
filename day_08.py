from helper import get_input

inp = get_input(day=8)

forest = [[int(x) for x in trees] for trees in inp]
m = len(forest)
n = len(forest[0])

def part_1():
    visible = set()

    for i in range(1, m-1):
        left = [0] * n
        right = [0] * n

        left[0] = forest[i][0]
        for j in range(1, n):
            left[j] = max(left[j - 1], forest[i][j])

        right[-1] = forest[i][-1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], forest[i][j])

        for j in range(1, n - 1):
            if forest[i][j] > left[j-1] or forest[i][j] > right[j+1]:
                visible.add((i, j))

    for j in range(1, n-1):
        left = [0] * m
        right = [0] * m

        left[0] = forest[0][j]
        for i in range(1, m):
            left[i] = max(left[i - 1], forest[i][j])

        right[-1] = forest[-1][j]
        for i in range(m - 2, -1, -1):
            right[i] = max(right[i + 1], forest[i][j])

        for i in range(1, m - 1):
            if forest[i][j] > left[i-1] or forest[i][j] > right[i+1]:
                visible.add((i, j))
    return len(visible) + 2*n + 2*m - 4

print(f"D08P1: {part_1()}")
