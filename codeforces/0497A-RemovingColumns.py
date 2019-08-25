n, m = map(int, input().split())

table = [input() for _ in range(n)]
ans = 0
col = 0

for i in range(m):
    if all(a[:col+1] <= b[:col+1] for a, b in zip(table, table[1:])):
        col += 1
    else:
        ans += 1
        table = [a[:col] + a[col+1:] for a in table]

print(ans)
