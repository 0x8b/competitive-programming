import math

w, h, a = map(int, input().strip().split())

if h > w:
    w, h = h, w

if a > 90:
    a = 90 - (a - 90)

a = math.radians(a)

if a < 2 * math.atan2(h, w):
    area = w * h

    s = (w / 2) - (h / 2 * math.tan(a / 2))
    bigger_area = 0.5 * s * s * math.tan(a)

    s = (h / 2) - (w / 2 * math.tan(a / 2))
    lower_area = 0.5 * s * s * math.tan(a)

    print(area - 2 * bigger_area - 2 * lower_area)
else:
    print(h * h / math.sin(a))
