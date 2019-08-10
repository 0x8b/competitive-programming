n = int(input())

for _ in range(n):
    px, py, qx, qy = map(int, input().split())

    rx = qx + qx - px
    ry = qy + qy - py

    print(rx, ry)
