from collections import Counter

n, k = map(int, input().split())

l = list(map(lambda x: int(x) % k, input().rstrip().split()))

ans = len(l)

s = set(l)
c = Counter(l)

pairs = set(tuple(sorted([k - i, i])) for i in s if ((k - i) in s) and (i != k - i))

for p in pairs:
    ans -= min(c[p[0]], c[p[1]])

if 0 in s:
    ans = ans + 1 - c[0]

if k % 2 == 0 in s:
    ans = ans + 1 - c[k // 2]

if k == 1:
    ans = 1

print(ans)
