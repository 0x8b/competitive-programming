n, m, h = map(int, input().split())

f = list(map(int, input().split())) # front
l = list(map(int, input().split())) # left

for y in range(n):
    row = input().split()

    print(' '.join([str(min(f[x], l[y]) if c is '1' else 0) for x, c in enumerate(row)]))
