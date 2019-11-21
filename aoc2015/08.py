#!/usr/bin/env python

import re
import fileinput

total = 0
encoded_total = 0

f = re.compile(r'\\"|\\\\|\\x[0-9a-f][0-9a-f]|[a-z]')

strings = [line.strip() for line in fileinput.input()]

for s in strings:
    total += len(s) - len(f.findall(s[1:-1]))

    encoded_total += len(s) + 2 + s.count("\\") + s.count('"')

assert total == 1333

ans = encoded_total - sum(map(len, strings))

assert ans == 2046
