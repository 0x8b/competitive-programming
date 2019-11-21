#!/usr/bin/env python

polymer = input()

letters = [ord(c) for c in set(polymer.upper())]

polymer = [ord(c) for c in polymer]


def react(polymer, forbidden=set()):
    stack = []

    for unit in polymer:
        if unit not in forbidden:
            if stack and abs(unit - stack[-1]) == 32:
                stack.pop()
            else:
                stack.append(unit)

    return len(stack)


assert react(polymer) == 9172

lowest = min([react(polymer, {c, c + 32}) for c in letters])

assert lowest == 6550
