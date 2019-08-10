q = int(input())

for _ in range(q):
    s = input()
    l = len(s)

    prev = s[0]
    cnt = 1

    for ch in s:
        if ch != prev:
            prev = ch
            cnt += 1

    print(len(s) - cnt)
