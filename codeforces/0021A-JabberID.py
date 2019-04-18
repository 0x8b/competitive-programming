#! python

import re

p = re.compile(r"^[A-Za-z0-9_]{1,16}@([A-Za-z0-9_\.]{1,32})(\/[A-Za-z0-9_]{1,16})?$")

match = p.match(input())

match = match and all(0 < len(s) <= 16 for s in match.group(0).split(sep = '.'))

print('YES' if match else 'NO')
