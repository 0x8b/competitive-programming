n = int(input())

for _ in range(n):
    _, s = input(), input()

    ans = 0

    if s[0] == "<" and s[-1] == ">":
        ans = min(s.index(">"), s[::-1].index("<"))

    print(ans)
