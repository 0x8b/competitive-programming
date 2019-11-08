import math

t = int(input())


def product(start, end):
    return math.prod(range(start, end + 1))


for _ in range(t):
    n, r = map(int, input().split())

    # nCr
    ans = product(n + 1, n + r) // product(1, r)

    print(ans % 1000000007)
