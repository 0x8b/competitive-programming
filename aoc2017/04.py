#!/usr/bin/env python

import fileinput

valid_1 = 0
valid_2 = 0

for passphrase in fileinput.input():
    parts = passphrase.split()

    if len(parts) == len(set(parts)):
        valid_1 += 1

    s = set(''.join(sorted(p)) for p in parts)

    if len(parts) == len(s):
        valid_2 += 1

assert valid_1 == 455
assert valid_2 == 186
