import itertools
import os

l = int(input())
r = int(input())

m = max(map(lambda x: x[0] ^ x[1], itertools.combinations(range(l, r + 1), 2)))

print(m)
