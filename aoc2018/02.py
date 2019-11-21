#!/usr/bin/env python

import fileinput
from collections import Counter

ids = [line.strip() for line in fileinput.input()]

ids.sort()

two = 0
three = 0

for d in ids:
    cc = Counter(d).values()

    two += 2 in cc
    three += 3 in cc

assert two * three == 9139

for a, b in zip(ids, ids[1:]):
    c = "".join(d for d, e in zip(a, b) if d != e)

    if len(c) == len(ids[0]) - 1:
        assert c == "uqcidadzwtnhsljvxyobmkfyr"
        break
