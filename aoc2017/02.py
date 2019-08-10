#!/usr/bin/env python

import fileinput
import itertools

checksum = 0
result = 0

for row in fileinput.input():
    values = list(map(int, row.strip().split()))

    checksum += max(values) - min(values)

    for a, b in itertools.combinations(sorted(values), 2):
        d, m = divmod(b, a)

        if m == 0:
            result += d
            break

assert checksum == 48357
assert result == 351
