n = int(input())
s = list(input())

a, p, c = 0, 0, 0

for d in s:
    p = c
    c += 1 if d == 'U' else -1
    a += 1 if p == -1 and c == 0 else 0

print(a)
