q = int(input())

for _ in range(q):
    s = list(map(ord, input()))
    r = list(reversed(s))

    a = [abs(a - b) for a, b in zip(s[1:], s)]
    b = [abs(a - b) for a, b in zip(r[1:], r)]

    print("Funny" if a == b else "Not Funny")
