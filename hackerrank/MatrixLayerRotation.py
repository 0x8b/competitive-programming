#! python

import numpy as np

m, n, rot = map(int, input().rstrip().split())

a = np.array([list(map(int, input().rstrip().split())) for _ in range(m)], dtype='uint32')

if m != n and min(m, n) == m:
    a = a.T

h, w = a.shape

h = h - 2

for i in range(w // 2):
    t = a[   i,      i:i+w]
    b = a[-1-i,      i:i+w]
    l = a[1+i:1+i+h,     i]
    r = a[1+i:1+i+h,  -1-i]

    s = np.concatenate((t, r, np.flip(b), np.flip(l)))

    s = np.roll(s, -rot % s.size)

    # top
    a[i, i:i+w] = s[:w]
    s = s[w:]

    # right
    a[1+i:1+i+h, -1-i] = s[:h]
    s = s[h:]

    # bottom
    a[-1-i, i:i+w] = np.flip(s[:w])
    s = s[w:]

    # left
    a[1+i:1+i+h, i] = np.flip(s)

    w = w - 2
    h = h - 2


for row in a:
    print(' '.join(map(str, row)))
