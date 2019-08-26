from itertools import groupby

t = input()

row = input().split()

row = [len(list(g)) for k, g in groupby(row)]

ans = 2 * max(min(a, b) for a, b in zip(row, row[1:]))

print(ans)
