#!/usr/bin/env python

import fileinput
from collections import Counter

data = [list(line.strip()) for line in fileinput.input()]
data = ["".join(a) for a in zip(*data)]


def ans(mode):
    return "".join(Counter(a).most_common()[mode][0] for a in data)


assert ans(0) == "gebzfnbt"
assert ans(-1) == "fykjtwyn"
