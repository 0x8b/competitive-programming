#! python

n = int(input())

a = list(map(int, input().split()))

s1, s2 = set(), set()

ans = True


for i in a:
    if i not in s1:
        s1.add(i)
    elif i not in s2:
        s2.add(i)
    else:
        ans = False
        break


if ans:
    a.sort()

    asc, desc = [], []

    for i, el in enumerate(a):
        (asc, desc)[i & 1].append(el)

    desc = list(reversed(desc))

    print('YES')
    print(len(asc))
    print(' '.join(map(str, asc)))
    print(len(desc))
    print(' '.join(map(str, desc)))
else:
    print('NO')
