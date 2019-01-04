import math

q = int(input())

for _ in range(q):
    a, b = map(lambda x: math.sqrt(int(x)), input().split())

    print(1 + math.floor(b) - math.ceil(a))
