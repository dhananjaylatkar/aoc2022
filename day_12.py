from helper import get_input
from pprint import pprint

inp = get_input(day=12)

grid = [[ord(x) - ord("a") for x in rows] for rows in inp]
M = len(grid)
N = len(grid[0])
S = None
E = None
for i, row in enumerate(grid):
    try:
        s_idx = row.index(ord("S") - ord("a"))
        S = (i, s_idx)
    except ValueError:
        pass
    try:
        e_idx = row.index(ord("E") - ord("a"))
        E = (i, e_idx)
    except ValueError:
        pass

grid[S[0]][S[1]] = 0  # a
grid[E[0]][E[1]] = 25  # z


def bfs(starts, end):
    q = []
    visited = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for s in starts:
        visited.add(s)
        q.append((s[0], s[1], 0))

    while q:
        l = len(q)

        for _ in range(l):
            x, y, dist = q.pop(0)
            for d in dirs:
                _x = x + d[0]
                _y = y + d[1]
                new_point = (_x, _y)
                if (
                    _x >= 0
                    and _x < M
                    and _y >= 0
                    and _y < N
                    and grid[_x][_y] - grid[x][y] <= 1
                    and new_point not in visited
                ):
                    visited.add(new_point)
                    q.append((_x, _y, dist + 1))
                    if new_point == end:
                        return dist + 1


def part_1():
    return bfs([S], E)


def part_2():
    starts = set()
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == 0:
                starts.add((i, j))
    return bfs(starts, E)


print(f"D12P1: {part_1()}")
print(f"D12P2: {part_2()}")
