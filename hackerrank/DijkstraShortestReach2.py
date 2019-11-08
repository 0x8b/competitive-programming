from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    e = [tuple(map(int, input().rstrip().split())) for _ in range(m)]

    s = int(input())

    # Bellman–Ford algorithm
    p = defaultdict(lambda: None)  # predecessor
    d = defaultdict(lambda: float('inf'))  # distance

    d[s] = 0

    for _ in range(n - 1):
        for f, t, w in e:  # from, to, weight
            if d[t] > d[f] + w:
                d[t] = d[f] + w
                p[t] = f

            if d[f] > d[t] + w:
                d[f] = d[t] + w
                p[f] = t

    out = [d[n] if d[n] != float('inf') else -1 for n in range(1, n + 1) if n != s]

    print(*out)
