#!/usr/bin/env python

import fileinput
import hashlib

door_id = next(fileinput.input()).strip()
password = ""
p = [None] * 8
i = 0

while True:
    while True:
        hash = hashlib.md5((door_id + str(i)).encode("ascii")).hexdigest()
        i += 1

        if hash.startswith(5 * "0"):
            index = int(hash[5], 16)

            password += hash[5]

            if index <= 7:
                if p[index] is None:
                    p[index] = hash[6]

            break

    if None in p:
        continue

    break

assert "d4cd2ee1" == password[:8]
assert "f2c730e5" == "".join(p)
