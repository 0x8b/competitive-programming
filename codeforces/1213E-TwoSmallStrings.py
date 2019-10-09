from itertools import permutations
import sys

n = int(input())
s = input()
t = input()

for p in permutations('abc', 3):
    a = n * ''.join(p)
    b = ''.join(n * c for c in p)

    if s not in a and t not in a:
        print('YES')
        print(a)
        sys.exit()
    elif s not in b and t not in b:
        print('YES')
        print(b)
        sys.exit()

print('NO')
