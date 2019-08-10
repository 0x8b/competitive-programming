n = int(input())

steps = []

mx, my = 1e6, 1e6

for _ in range(n):
    x, y = map(int, input().rstrip().split())

    mx = min(x, mx)
    my = min(y, my)

print(mx * my)
