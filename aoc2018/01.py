#!/usr/bin/env python

import fileinput
import itertools

nums = [int(line) for line in fileinput.input()]

total = sum(nums)
seen = set()
dbl = None

for k in itertools.accumulate(itertools.cycle(nums)):
    if k in seen:
        dbl = k
        break

    seen.add(k)

assert total == 477
assert dbl == 390
