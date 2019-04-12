#! python

from itertools import groupby

m = max(len(list(g)) for k, g in groupby(input()))

print('YES' if m >= 7 else 'NO')
