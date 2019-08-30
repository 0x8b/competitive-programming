t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))[::-1]

    m = prices[0]
    c = 0

    for p in prices[1:]:
        c += p > m
        m = min(m, p)

    print(c)
