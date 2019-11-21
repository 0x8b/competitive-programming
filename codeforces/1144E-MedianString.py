from string import ascii_lowercase


def dec2az(n: int) -> str:
    out = ""

    while n:
        mod = (n - 1) % 26
        n = (n - mod) // 26
        out += ascii_lowercase[mod]

    return out[::-1]


def az2dec(s: str) -> int:
    out = 0

    for p, c in enumerate(s[::-1]):
        out += 26 ** p * (ord(c) - ord("a") + 1)

    return out


_ = input()
s = input()
t = input()

median = (az2dec(s) + az2dec(t)) // 2

print(dec2az(median))
