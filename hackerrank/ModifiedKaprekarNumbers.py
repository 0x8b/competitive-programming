p = int(input())
q = int(input())

invalid = True

for n in range(p, q + 1):
    d = len(str(n))
    s = str(n * n)
    m = len(s)

    if n == int("0" + s[: m - d]) + int(s[m - d :]):
        invalid = False
        print(n, end=" ")

if invalid:
    print("INVALID RANGE")
