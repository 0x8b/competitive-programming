#!/usr/bin/env python

import fileinput

keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

bathroom_keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]

x, y = 1, 1
bx, by = 0, 2

code = ""
bathroom_code = ""

for instr in fileinput.input():
    for d in instr.strip():
        if d == "U":
            y = max(0, y - 1)
        elif d == "D":
            y = min(2, y + 1)
        elif d == "R":
            x = min(2, x + 1)
        else:
            x = max(0, x - 1)

    code += str(keyboard[y][x])

    for d in instr.strip():
        if d == "U":
            ny = max(0, by - 1)

            if bathroom_keypad[ny][bx] != 0:
                by = ny
        elif d == "D":
            ny = min(4, by + 1)

            if bathroom_keypad[ny][bx] != 0:
                by = ny
        elif d == "R":
            nx = min(4, bx + 1)

            if bathroom_keypad[by][nx] != 0:
                bx = nx
        else:
            nx = max(0, bx - 1)

            if bathroom_keypad[by][nx] != 0:
                bx = nx

    bathroom_code += str(bathroom_keypad[by][bx])

assert "47978" == code
assert "659AD" == bathroom_code
