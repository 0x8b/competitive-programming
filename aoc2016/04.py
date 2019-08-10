#!/usr/bin/env python

import re
import string
import fileinput
from collections import Counter
from functools import cmp_to_key

structure = re.compile(r'^((\w+-)+)(\d+)\[(\w+)\]$')


def cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1


cmp_items = cmp_to_key(cmp)
s = 0
north_object_id = None

for line in fileinput.input():
    name, sector_id, checksum = structure.fullmatch(line.strip()).group(1, 3, 4)

    sector_id = int(sector_id)

    cc = Counter(name.replace('-', ''))

    cc = cc.most_common()
    cc.sort(key=cmp_items)

    if checksum == ''.join([e[0] for e in cc[:5]]):
        s += sector_id

    name = name.replace('-', ' ').strip()
    shift = sector_id % 26
    az = string.ascii_lowercase
    name = name.translate(str.maketrans(az, az[shift:] + az[:shift]))

    if 'north' in name:
        north_object_id = sector_id


assert s == 409147
assert north_object_id == 991
