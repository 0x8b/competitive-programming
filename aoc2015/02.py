#!/usr/bin/env python

import fileinput

dims = [tuple(map(int, line.split('x'))) for line in fileinput.input()]

area = []
ribbon = []

for l, w, h in dims:
    l, w, h = sorted((l, w, h))

    extra = l * w
    area.append(2 * (l * w + w * h + l * h) + extra)
    ribbon.append(2 * (l + w) + (l * w * h))

total = sum(area)

assert total == 1606483

total = sum(ribbon)

assert total == 3842356
