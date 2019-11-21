from collections import deque

n, k = map(int, input().strip().split())

m = deque()
s = set()
c = 0

for a in list(map(int, input().strip().split())):
    if a in s:
        continue

    c = c + 1
    m.appendleft(a)
    s.add(a)

    if c > k:
        s.remove(m.pop())
        c = c - 1

print(len(m))
print(" ".join(map(str, m)))
