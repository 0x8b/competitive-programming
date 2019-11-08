t1, t2, n = map(int, input().split())

d = {1: t1, 2: t2}


def fib(n):
    if n in d:
        return d[n]
    else:
        a = fib(n - 1) ** 2 + fib(n - 2)
        d[n] = a
        return a


print(fib(n))
