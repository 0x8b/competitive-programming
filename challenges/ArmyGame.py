from math import ceil

n, m = map(int, input().split())

s = ceil(n / 2) * ceil(m / 2)

print(s)
