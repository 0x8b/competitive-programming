#!/usr/bin/env python

import fileinput

stream = next(fileinput.input())

s = 0  # state
stack = 0
total = 0

counter = 0

for ch in stream:
    if s == 0:
        if ch == "{":
            stack += 1
        elif ch == "}":
            total += stack
            stack -= 1
        elif ch == "<":
            s = 1
    elif s == 1:
        if ch == "!":
            s = 2
        elif ch == ">":
            s = 0
        else:
            counter += 1
    elif s == 2:
        s = 1


assert total == 16869
assert counter == 7284
