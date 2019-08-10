p, d, m, s = map(int, input().split())

a = 0
i = 0

while a <= s:
    a += max(p - i * d, m)
    i += 1

print(i - 1)
