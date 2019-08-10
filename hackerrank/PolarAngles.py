from functools import cmp_to_key
from math      import pi, atan2, hypot

n = int(input())

coordinates = []

for _ in range(n):
    coordinates.append(list(map(int, input().rstrip().split())))

def polar_sort(a, b):
    ax, ay = a
    bx, by = b

    a_angle = atan2(ay, ax)
    b_angle = atan2(by, bx)

    if ay < 0: a_angle += 2 * pi
    if by < 0: b_angle += 2 * pi

    if a_angle == b_angle:
        return hypot(ax, ay) - hypot(bx, by)
    else:
        return a_angle - b_angle

coordinates.sort(key = cmp_to_key(polar_sort))

for x, y in coordinates:
    print(x, y)
