from collections import defaultdict

n, k = map(int, input().split())

nums = list(map(int, input().split()))

cc = defaultdict(int)
aa = defaultdict(list)

for num in nums:
    o = num
    i = 0

    while o != 0:
        cc[o] += 1
        aa[o].append(i)
        i += 1
        o //= 2

m = min(sum(sorted(aa[key])[:k]) for key, count in cc.items() if count >= k)

print(m)
