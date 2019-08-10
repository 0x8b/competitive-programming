from math import ceil

b, a = map(int, input().strip().split(' '))

print(ceil(a / (b / 2)))
