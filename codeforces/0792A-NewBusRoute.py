n = input()
a = sorted(map(int, input().strip().split()))

d = [c2 - c1 for c1, c2 in zip(a, a[1:])]
m = min(d)

print(f'{m} {d.count(m)}')
