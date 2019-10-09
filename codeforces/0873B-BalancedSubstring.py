from itertools import accumulate

n = int(input())
s = input().strip()

a = [0] + list(accumulate(2 * int(d) - 1 for d in list(s)))
m = {}

for i in range(len(a)):
    if a[i] not in m:
        m[a[i]] = i

    a[i] = i - m[a[i]]

print(max(a))
