from itertools import accumulate as acc

n1, n2, n3 = map(int, input().split())  # useless

s = [set(acc(map(int, reversed(input().strip().split())))) for _ in range(3)]

s = set.intersection(*s)

print(max(s) if len(s) > 0 else 0)
