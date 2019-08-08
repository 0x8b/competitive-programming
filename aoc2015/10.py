#!/usr/bin/env python

from itertools import groupby

digits = input().strip()


def look_and_say(n):
    s = digits

    for _ in range(n):
        parts = [list(g) for k, g in groupby(s)]

        s = ''.join([str(len(part)) + part[0] for part in parts])

    print(len(s))


assert look_and_say(40) == 492982
assert look_and_say(50) == 6989950
