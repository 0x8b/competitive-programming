n, m = map(int, input().strip().split())

p = list(map(int, input().strip().split()))

out = []

for i in range(n):
    pp = p[:]
    pp[i:i + 1] = []
    pp.insert(0, p[i])

    out.append(
        sum(abs(a - b) for a, b in zip(pp, pp[1:]))
    )

print(' '.join(map(str, out)))
