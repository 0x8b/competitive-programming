import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    m = m - 1

    a = math.prod(range(n + 1, n + m + 1))
    b = math.prod(range(1, m + 1))

    if m == 0:
        print(1)
    else:
        print((a // b) % 1000000007)
