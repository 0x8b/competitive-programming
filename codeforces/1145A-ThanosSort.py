#! python

from itertools import takewhile

import math

n = int(input())

arr = list(map(int, input().split()))

m = 0

def check(a):
    global m

    if a == sorted(a):
        m = max(m, len(a))
    else:
        p = len(a) // 2

        return check(a[:p]) or check(a[p:])

check(arr)

print(m)
