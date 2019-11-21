#!/usr/bin/env python

import re

password = input().strip()

zz = re.compile(r"\w[z]*$")
dup = re.compile(r"(\w)\1")


def increase(s):
    if s[-1] == "z":
        next_char = "a"

        if found := zz.search(s[:-1]):
            b = found.start(0)
            c = chr(ord(s[b]) + 1)
            s = s[:b] + c + ("a" * (len(s) - (b + 1)))
    else:
        next_char = chr(ord(s[-1]) + 1)

    return s[:-1] + next_char


def search(p):
    while True:
        p = increase(p)

        if len(dup.findall(p)) < 2:
            continue

        if "i" in p or "l" in p or "o" in p:
            continue

        diff = ["1" if (ord(b) - ord(a)) == 1 else "0" for a, b in zip(p, p[1:])]

        if "11" in "".join(diff):
            return p


ans = search(password)

assert "hxbxxyzz" == ans
assert "hxcaabcc" == search(ans)
