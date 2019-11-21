#!/usr/bin/env python

import fileinput

import numpy as np

pts = np.array([tuple(map(int, line.split(", "))) for line in fileinput.input()])

pts -= pts.min(axis=0)

shape = pts.max(axis=0) + 1

mht_dst = lambda a, b, c, d: abs(a - c) + abs(b - d)

# part 1

space = np.ndarray(shape, dtype=np.uint8)

for x in range(0, shape[0]):
    for y in range(0, shape[1]):
        dst = [mht_dst(x, y, px, py) for px, py in pts]

        m = min(dst)

        space[x, y] = dst.index(m) if dst.count(m) == 1 else 255


ids_on_border = set(space[[0, -1], :].flat) | set(space[:, [0, -1]].flat)

counter = np.bincount(space.flat)

counter[list(ids_on_border)] = 0

counter.resize((255,))

assert counter.max() == 3882

# part 2

f = lambda x, y: sum(mht_dst(x, y, px, py) for px, py in pts)

space = np.fromfunction(f, shape) < 10000

assert space.sum() == 43852
