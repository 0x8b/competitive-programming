#!/usr/bin/env python

import re
import fileinput


strings = [s for s in fileinput.input()]

twice = re.compile(r"(\w)\1")
forbidden = re.compile(r"ab|cd|pq|xy")

nice = 0

for string in strings:
    if len([c for c in string if c in "aeiou"]) >= 3:
        if twice.search(string):
            if not forbidden.search(string):
                nice += 1

assert nice == 258

pair = re.compile(r"(\w\w).*\1")
letter_between = re.compile(r"(\w)\w\1")

nice = 0

for string in strings:
    if pair.search(string):
        if letter_between.search(string):
            nice += 1

assert nice == 53
