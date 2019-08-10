t = int(input())

for _ in range(t):
    n = int(input())
    y = True

    grid = []

    for _ in range(n):
        grid.append(sorted(list(input())))

    transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    # better
    transposed = list(zip(*grid))

    for row in transposed:
        if row != tuple(sorted(row)):
            y = False
            break

    print("YES" if y else "NO")
