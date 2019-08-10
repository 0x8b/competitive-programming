import itertools as it

l = int(input().strip())
s = list(input())

m = 0

for ch1, ch2 in it.combinations(set(s), 2):
    f = [c for c in s if (c == ch1 or c == ch2)]

    if all([a != b for a, b in zip(f, f[1:])]):
        m = max(m, len(f))

print(m)
