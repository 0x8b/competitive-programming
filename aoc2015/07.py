#!/usr/bin/env python

import fileinput
from functools import lru_cache

d = dict(tuple(line.strip().split(' -> ')[::-1]) for line in fileinput.input())

bit = 0xffff


@lru_cache(maxsize=500)
def run(wire):
    if wire.isdigit():
        return int(wire)

    b = d[wire].split()

    if len(b) == 1:
        if b[0] in d:
            return run(b[0])
        elif b[0].isdigit():
            return int(b[0])
    elif len(b) == 2:
        if b[0] == 'NOT':
            return ~int(run(b[1])) & bit
    elif len(b) == 3:
        if b[1] == 'AND':
            return (run(b[0])  & run(b[2])) & bit
        elif b[1] == 'OR':
            return (run(b[0])  | run(b[2])) & bit
        elif b[1] == 'LSHIFT':
            return (run(b[0]) << run(b[2])) & bit
        elif b[1] == 'RSHIFT':
            return (run(b[0]) >> run(b[2])) & bit


ans = run('a') & bit

assert ans == 46065

d['b'] = str(ans)

run.cache_clear()

ans = run('a') & bit

assert ans == 14134
