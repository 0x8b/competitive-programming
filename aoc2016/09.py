#!/usr/bin/env python

import re

file = input()

pair = re.compile(r'\((\d+)x(\d+)\)')

decompressed = ''

while True:
    match = pair.match(file)

    if match:
        a, b = map(int, match.group(1, 2))

        file = file[match.end(2) + 1:]

        decompressed += file[:a] * b
        file = file[a:]

    index = file.find('(')

    if index == -1:
        decompressed += file

        break

    decompressed += file[:index]
    file = file[index:]

assert len(decompressed) == 183269
