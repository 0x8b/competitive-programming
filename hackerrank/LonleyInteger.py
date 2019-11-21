n = int(input())
a = list(map(int, input().rstrip().split()))

unique = 0

for i in a:
    unique ^= i

print(unique)

# alternative

import operator as op
import functools as ft

lonley_integer = ft.reduce(op.xor, a, 0)

print(lonley_integer)
