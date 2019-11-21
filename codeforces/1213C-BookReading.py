q = int(input())

for _ in range(q):
    n, m = map(int, input().split())

    d = n // m
    a = [0] * 10

    for i in range(10):
        a[i] = (m + a[i - 1]) % 10

    s = sum(a)

    print((d // 10) * s + sum(a[: (d % 10)]))
