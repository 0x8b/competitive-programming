import functools
import operator

index, position = 0, 0
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

xor = functools.reduce(operator.xor, [row[0] for row in matrix])

yes = xor > 0 or any(len(set(row)) > 1 for row in matrix)

if yes and xor == 0:
    for i, row in enumerate(matrix):
        if len(set(row)) > 1:
            for j, number in enumerate(row):
                if row[0] != number:
                    index, position = i, j + 1
                    break
            break

print("TAK" if yes else "NIE")

if yes:
    indices = ["1"] * n
    indices[index] = str(position)
    print(" ".join(indices))
