import functools
import operator

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    if n & 1:
        ans = functools.reduce(operator.xor, arr[::2], 0)
    else:
        ans = 0

    print(ans)
