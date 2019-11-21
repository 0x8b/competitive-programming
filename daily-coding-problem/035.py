#!/usr/bin/env python

"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second, and the
Bs come last. You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

from random import randint, shuffle

s = list("R" * randint(0, 10) + "G" * randint(0, 10) + "B" * randint(0, 10))
a = s[:]

shuffle(a)

print("".join(a))  # print unsorted array

# pointers
r = 0
p = 0
b = len(a) - 1

while p <= b:
    if a[p] == "G":
        p += 1

    elif a[p] == "R":
        a[r], a[p] = a[p], a[r]
        p += 1
        r += 1

    elif a[p] == "B":
        a[b], a[p] = a[p], a[b]
        b -= 1

print("".join(a))  # print sorted array
