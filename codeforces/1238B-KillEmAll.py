from collections import deque

q = int(input())

for _ in range(q):
    n, r = map(int, input().strip().split())
    x = input().strip().split()

    d = deque(sorted(set(map(int, x))))
    counter = 0

    while d:
        d.pop()

        while d and d[0] - (counter + 1) * r <= 0:
            d.popleft()

        counter += 1

    print(counter)
