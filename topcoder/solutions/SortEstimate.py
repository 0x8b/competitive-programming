#!/usr/bin/env python

import math


def how_many(c, time):
    assert 1 <= c <= 100
    assert 1 <= time <= 2000000000

    left, right = 1, 2000000000

    while not right - left < 1e-9:
        n = (left + right) / 2

        if n * math.log(n, 2) >= time / c:
            right = n
        else:
            left = n

    return left


assert abs(how_many(1, 8) - 4) < 1e-9
assert abs(how_many(2, 16) - 4) < 1e-9
assert abs(how_many(37, 12392342) - 23104.999312341137) < 1e-9
assert abs(how_many(1, 2000000000) - 7.637495090348122E7) < 1e-9
