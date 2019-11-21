#!/usr/bin/env python

import fileinput
import re

import numpy as np

fabric = np.zeros((1000, 1000), dtype=np.int)
num = re.compile(r"\d+")

data = [tuple(map(int, num.findall(claim))) for claim in fileinput.input()]

for _, l, t, w, h in data:
    fabric[t : t + h, l : l + w] += 1

s = len(fabric[fabric > 1])

assert s == 116489

found = None

for id, l, t, w, h in data:
    if np.sum(fabric[t : t + h, l : l + w]) == w * h:
        found = id
        break

assert found == 1260
