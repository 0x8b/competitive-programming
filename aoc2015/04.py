#!/usr/bin/env python

from hashlib import md5

secret = input().strip()

i = 0

while True:
    if md5((secret + str(i)).encode("ascii")).hexdigest().startswith(5 * "0"):
        five = i
        break

    i += 1

assert five == 254575


while True:
    if md5((secret + str(i)).encode("ascii")).hexdigest().startswith(6 * "0"):
        six = i
        break

    i += 1

assert six == 1038736
