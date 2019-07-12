t = int(input())

for _ in range(t):
    n, s, t = map(int, input().split())

    c = s + t - n
    s = s - c
    t = t - c

    print(max(s, t) + 1)
