#!/usr/bin/env python

import fileinput

program = [line.strip().replace(",", "").split() for line in fileinput.input()]

regs = {"a": 1, "b": 0}
pc = 0

while True:
    if pc >= len(program):
        break

    c, d = program[pc][:2]

    if c == "hlf":
        regs[d] //= 2
    elif c == "tpl":
        regs[d] *= 3
    elif c == "inc":
        regs[d] += 1
    elif c == "jmp":
        pc += int(d)
        continue
    elif c == "jie":
        pc += int(program[pc][2]) if regs[d] % 2 == 0 else 1
        continue
    elif c == "jio":
        pc += int(program[pc][2]) if regs[d] == 1 else 1
        continue

    pc += 1

assert regs["b"] == 307
assert regs["b"] == 160
