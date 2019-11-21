import os

n = int(input())
arr = list(map(int, input().rstrip().split()))

l = len(arr)
p = n = z = 0

for i in arr:
    if i < 0:
        n += 1
    elif i > 0:
        p += 1
    else:
        z += 1

print("\n".join(map(lambda x: "{0:.6f}".format(x / l), [p, n, z])))
