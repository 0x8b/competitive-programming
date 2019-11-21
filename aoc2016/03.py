#!/usr/bin/env python

import fileinput

import numpy as np

data = []

for line in fileinput.input():
    data.append(list(map(int, line.strip().split())))


def count(data):
    triangles = 0

    for a, b, c in data:
        if a + b > c and a + c > b and b + c > a:
            triangles += 1

    return triangles


assert count(data) == 982

data = np.reshape(np.array(data).T, (-1, 3))

assert count(data) == 1826
