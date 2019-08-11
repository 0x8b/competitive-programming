#!/usr/bin/env python

import re
import fileinput

abba = re.compile(r'(\w)(\w)\2\1')
aba = re.compile(r'(?=((\w)\w\2))')

b = re.compile(r'\b')

tls_counter = 0
ssl_counter = 0

for ip in fileinput.input():
    parts = [p for p in b.split(ip.strip()) if p not in ('', '[', ']')]

    supp = ','.join(parts[::2])
    nets = ','.join(parts[1::2])

    tls = False

    if any(a[0] != a[1] for a in abba.findall(supp) or []):
        tls = True

    if any(a[0] != a[1] for a in abba.findall(nets) or []):
        tls = False

    tls_counter += tls

    a = set(a.group(1) for a in aba.finditer(supp))
    r = set([a.group(1)[1] + a.group(1)[:2] for a in aba.finditer(nets) or []])

    ssl_counter += a & r

assert tls_counter == 115
assert ssl_counter == 231
