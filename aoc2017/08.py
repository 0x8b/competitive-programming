#!/usr/bin/env python

import fileinput

from collections import defaultdict

reg = defaultdict(int)
max_ever = float('-inf')
cond = False

for instr in fileinput.input():
    a, op, b, _, c, op2, d = instr.split(' ')

    exec(f'global cond; cond = {reg[c]} {op2} {d}')

    if cond:
        reg[a] += int(b) if op == 'inc' else -int(b)

    max_ever = max(max_ever, max(reg.values()))

assert 2971 == max(reg.values())
assert 4254 == max_ever
