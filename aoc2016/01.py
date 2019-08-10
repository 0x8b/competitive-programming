#!/usr/bin/env python

instr = input().strip().split(', ')

instr = [(s[0], int(s[1:])) for s in instr]

turn_right = 0 - 1j
turn_left = 0 + 1j

direction = 1  # North

position = 0 + 0j
found = None

visited = {position}

for d, dist in instr:
    if d == 'R':
        direction *= turn_right
    else:
        direction *= turn_left

    for i in range(dist):
        position += direction

        if not found and position in visited:
            found = position

        visited.add(position)

assert int(abs(position.real) + abs(position.imag)) == 273
assert int(abs(found.real) + abs(found.imag)) == 115
