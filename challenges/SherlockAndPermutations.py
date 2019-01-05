from functools import reduce
from operator import mul

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    m = m - 1

    a = reduce(mul, [i for i in range(n + 1, n + m + 1)], 1)
    b = reduce(mul, [i for i in range(1, m + 1)], 1)

    if m == 0:
        print(1)
    else:
        print((a // b) % 1000000007)
