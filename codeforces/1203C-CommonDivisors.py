from math import sqrt

n = input()

ints = list(set(map(int, input().strip().split())))

m = min(ints)

s = set(d for d in range(1, int(sqrt(m)) + 2) if m % d == 0)

s = s.union(set(m // d for d in s))

s.remove(1)

c = set(s)  # copy

for d in s:
    for i in ints:
        if i % d != 0:
            c.remove(d)
            break

print(len(c) + 1)
