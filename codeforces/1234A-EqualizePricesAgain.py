import math

q = int(input())

for _ in range(q):
    n = int(input())

    print(math.ceil(sum(map(int, input().strip().split())) / n))
