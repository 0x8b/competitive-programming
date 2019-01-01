i, j, k = map(int, input().split())

c = 0

for m in range(i, j + 1):
    if abs(m - int(str(m)[::-1])) % k == 0:
        c += 1

print(c)