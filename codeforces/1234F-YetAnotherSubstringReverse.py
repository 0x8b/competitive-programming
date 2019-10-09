import sys
from collections import defaultdict

s = input().strip()

letters = set(s)
seen = set()
last = defaultdict(int)
longest = [0] * len(s)
length = 0

for i, c in enumerate(s):
    if c in seen:
        seen.difference_update(set(s[i - length:last[c]]))
        length = i - last[c]
    else:
        length = length + 1
        seen.add(c)

    longest[i] = length
    last[c] = i

m = max(longest)
indexes = [i for i, e in enumerate(longest) if e == m]

kk = 0

if m == len(letters):
    print(m)
    sys.exit(0)

for i in indexes:
    substring = s[i - longest[i] + 1:i + 1]
    bb = letters - set(substring)
    cc = ''.join([ch if ch in bb else '-' for ch in s])
    mm = max([len(set(gg)) for gg in cc.split('-')])
    kk = max(len(substring) + mm, kk)

print(kk)


