import math

n, r = map(int, input().split())

sin_a = math.sin(math.pi / n)

R = r * sin_a / (1 - sin_a)

print(R)
