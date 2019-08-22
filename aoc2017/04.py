#!/usr/bin/env python

import fileinput

p = [p.split() for p in fileinput.input()]

assert sum(len(a) == len(set(a)) for a in p) == 455
assert sum(len(a) == len(set(''.join(sorted(b)) for b in a)) for a in p) == 186
