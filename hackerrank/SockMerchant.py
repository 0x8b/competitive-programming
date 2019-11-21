from collections import Counter

n = int(input())
ar = list(map(int, input().rstrip().split()))

# solution
c = sum(map(lambda x: x // 2, Counter(ar).values()))

# alternative solution
c = 0
s = set()

for sock in ar:
    if sock in s:
        s.remove(sock)
        c += 1
    else:
        s.add(sock)

print(c)
