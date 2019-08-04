#!/usr/bin/env python

from itertools import accumulate

instructions = input().strip()

direction = [1 if i == '(' else -1 for i in instructions]

assert sum(direction) == 280

floor = list(accumulate(direction)).index(-1) + 1

assert floor == 1797
