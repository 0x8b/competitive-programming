#! python

import re

r = re.compile(r"^[A-Za-z0-9_]{1,16}@([A-Za-z0-9_\.]{1,32})(\/[A-Za-z0-9_]{1,16})?$")

match = r.match(input())

yes = False

if match:
    hostname = match.group(1)

    if all(len(s) >= 1 and len(s) <= 16 for s in hostname.split(sep = '.')):
        yes = True

print('YES' if yes else 'NO')
