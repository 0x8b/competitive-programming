#!/usr/bin/env python

import fileinput

stream = next(fileinput.input())

state = 0
stack = 0
total = 0

counter = 0

for ch in stream:
    if state == 0:
        if ch == '{':
            stack += 1
        elif ch == '}':
            total += stack
            stack -= 1
        elif ch == '<':
            state = 1
    elif state == 1:
        if ch == '!':
            state = 2
        elif ch == '>':
            state = 0
        else:
            counter += 1
    elif state == 2:
        state = 1


assert total == 16869
assert counter == 7284
