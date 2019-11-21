#!/usr/bin/env python

from collections import Counter
from itertools import accumulate

moves = input().strip()


def c(m):
    return {"^": 0 + 1j, ">": 1 + 0j, "v": 0 - 1j, "<": -1 + 0j}[m]


def houses(moves):
    return list(accumulate([0j] + moves))


def at_least_one_present(locations):
    return len([h for h in Counter(locations).values() if h >= 1])


moves = [c(m) for m in moves]

assert at_least_one_present(houses(moves)) == 2592

s = houses(moves[::2])
r = houses(moves[1::2])

assert at_least_one_present(s + r) == 2360
