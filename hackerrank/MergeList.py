import operator
import functools

t = int(input())

def capital_pi(f, t):
    return functools.reduce(operator.mul, range(f, t + 1), 1)

for _ in range(t):
    n, r = map(int, input().split())

    n = n + r

    # nCr
    a = capital_pi(n - r + 1, n) // capital_pi(1, r)

    print(a % 1000000007)
