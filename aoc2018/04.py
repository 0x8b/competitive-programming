#!/usr/bin/env python

import collections
import fileinput
import operator
import re

import numpy as np

sorted_puzzle = "\n".join(
    sorted([line.rstrip() for line in fileinput.input()], key=lambda a: a[:17])
)

d = collections.defaultdict(lambda: np.zeros(60, dtype="uint"))

for shift in re.findall(r"\[.*G[^G]*\n", sorted_puzzle, re.MULTILINE):
    gid = int(re.search(r"#(\d+)", shift).group(1))
    minutes = np.array([int(r[15:17]) for r in shift.rstrip().split("\n")[1:]])

    if len(minutes) & 1:
        minutes = np.append(minutes, [60])

    for asleep, up in minutes.reshape(-1, 2):
        d[gid][asleep:up] += 1


summary = [(k, v.max(), v.sum()) for k, v in d.items()]

gid, _, _ = max(summary, key=operator.itemgetter(2))

assert gid * d[gid].argmax() == 30630

gid, _, _ = max(summary, key=operator.itemgetter(1))

assert gid * d[gid].argmax() == 136571
