#! python

import math

n, t = map(int, input().split())

minimum, index = float('inf'), 0

for i in range(n):
    s, d = map(int, input().split())

    time = s - t if t < s else (d - (t - s) % d if (t - s) % d else 0)

    if time < minimum:
        minimum, index = time, i + 1

print(index)
