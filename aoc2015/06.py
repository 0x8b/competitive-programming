#!/usr/bin/env python

import fileinput
import re

import numpy as np

number = re.compile(r"\d+")

lights1 = np.zeros((1000, 1000), np.bool_)
lights2 = np.zeros((1000, 1000), np.longlong)

for instr in fileinput.input():
    tlx, tly, brx, bry = map(int, number.findall(instr))

    brx += 1
    bry += 1

    if "turn on" in instr:
        lights1[tlx:brx, tly:bry] = True
        lights2[tlx:brx, tly:bry] += 1
    elif "turn off" in instr:
        lights1[tlx:brx, tly:bry] = False
        lights2[tlx:brx, tly:bry] -= 1
        lights2[lights2 < 0] = 0
    else:
        lights1[tlx:brx, tly:bry] = np.bitwise_not(lights1[tlx:brx, tly:bry])
        lights2[tlx:brx, tly:bry] += 2

assert lights1.sum() == 569999
assert lights2.sum() == 17836115
