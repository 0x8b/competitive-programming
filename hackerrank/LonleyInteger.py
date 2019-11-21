n = int(input())
a = list(map(int, input().rstrip().split()))

unique = 0

for i in a:
    unique ^= i

print(unique)

# alternative

import functools as ft
import operator as op

lonley_integer = ft.reduce(op.xor, a, 0)

print(lonley_integer)
