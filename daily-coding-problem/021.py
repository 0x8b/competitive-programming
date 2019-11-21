#!/usr/bin/env python

"""
Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from collections import defaultdict

lectures = [(30, 75), (0, 50), (60, 150)]

dd = defaultdict(lambda: {"close": 0, "open": 0})
timestamps = set()
required = 0
stack_top = 0

for start, end in lectures:
    timestamps |= {start, end}

    dd[start]["open"] += 1
    dd[end]["close"] += 1

timestamps = sorted(list(timestamps))

for point in timestamps:
    stack_top -= dd[point]["close"]
    stack_top += dd[point]["open"]

    required = max(required, stack_top)

print(required)  # 2

#### better

from collections import defaultdict

lectures = [(30, 75), (0, 50), (60, 150)]

dd = defaultdict(int)
required = 0
stack_top = 0

for start, end in lectures:
    dd[start] += 1
    dd[end] -= 1

dd = sorted(dd.items())

for k, v in dd:
    stack_top += v

    required = max(required, stack_top)

print(required)  # 2
