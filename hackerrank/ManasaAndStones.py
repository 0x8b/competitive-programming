T = int(input())

for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())

    s = set()

    for i in range(0, n):
        s.add(a * i + b * (n - 1 - i))

    print(*sorted(s))
