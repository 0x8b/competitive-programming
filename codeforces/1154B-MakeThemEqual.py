n = int(input())
a = map(int, input().split())
s = set(a)
a = list(sorted(s))

if len(s) > 3:
    print(-1)
elif len(s) == 3:
    if a[1] - a[0] == a[2] - a[1]:
        print(a[1] - a[0])
    else:
        print(-1)
elif len(s) == 2:
    if (a[1] - a[0]) % 2 == 0:
        print((a[1] - a[0]) // 2)
    else:
        print(a[1] - a[0])
else:
    print(0)
