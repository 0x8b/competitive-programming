import re
import string

upper = string.ascii_uppercase


def dec2az(n):
    out = ""

    while n:
        mod = (n - 1) % 26
        n = (n - mod) // 26
        out += upper[mod]

    return out[::-1]


def az2dec(s):
    out = 0

    for p, c in enumerate(s[::-1]):
        out += 26 ** p * (ord(c) - ord("A") + 1)

    return out


rc = re.compile(r"R(\d+)C(\d+)")
cr = re.compile(r"([A-Z]+)(\d+)")

n = int(input())

for _ in range(n):
    cell = input()

    if rc.match(cell):
        m = rc.search(cell)
        r = int(m.group(1))
        c = dec2az(int(m.group(2)))
        print(f"{c}{r}")

    else:
        m = cr.search(cell)
        c = az2dec(m.group(1))
        r = int(m.group(2))
        print(f"R{r}C{c}")
