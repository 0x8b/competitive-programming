from math import ceil, floor, sqrt

s = [c for c in input() if c != " "]

row = floor(sqrt(len(s)))
column = ceil(sqrt(len(s)))

if row * column < len(s):
    row += 1

s = s + [""] * column

for c in range(column):
    for r in range(row):
        print(s[r * column + c], end="")

    print(end=" ")
