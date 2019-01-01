from copy import copy, deepcopy

n = int(input())

grid = []

for _ in range(n):
    grid_item = list(input())
    grid.append(grid_item)

answer = deepcopy(grid) # [row[:] for row in grid]

for y in range(1, n - 1):
    for x in range(1, n - 1):
        c = grid[y][x]

        if c > grid[y - 1][x] and c > grid[y + 1][x] and c > grid[y][x - 1] and c > grid[y][x + 1]:
            answer[y][x] = 'X'

for row in answer:
    print(''.join(row))