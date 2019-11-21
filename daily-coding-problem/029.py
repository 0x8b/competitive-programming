#!/usr/bin/env python

"""
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded
as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string
to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

import re


s = input().strip()


def encode(s):
    s = s + "\n"
    last = s[0]
    li = 0
    o = ""

    for i in range(len(s)):
        if last != s[i]:
            o = o + str(i - li) + last
            last = s[i]
            li = i

    return o


def decode(s):
    p = re.compile("(\d+)([a-zA-Z])")
    o = ""

    for n, l in re.findall(p, s):
        o = o + int(n) * l

    return o


e = encode(s)
d = decode(e)

print("original:", s)
print("encoded: ", e)
print("decoded: ", d)
