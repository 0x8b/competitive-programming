#!/usr/bin/env python


def union_of_intervals(lower, upper, n):
    left = min(lower)
    right = max(upper)

    while left < right:
        mid = (left + right) // 2

        last_index = -1

        for l, r in zip(lower, upper):
            if l <= mid <= r:
                last_index += mid - l + 1
            elif r < mid:
                last_index += r - l + 1

        if last_index < n:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    import random
    import itertools

    assert union_of_intervals([1, 5], [3, 7], 4) == 6
    assert union_of_intervals([1, 3], [4, 5], 3) == 3
    assert union_of_intervals([-1500000000], [1500000000], 1500000091) == 91

    b = 10  # boundary

    num_of_intervals = random.randrange(1, 10)
    intervals = [
        (a := random.randrange(-b, b - 1), random.randrange(a + 1, b))
        for _ in range(num_of_intervals)
    ]
    lower, upper = zip(*intervals)

    arr = sorted(itertools.chain(*(range(f, t + 1) for f, t in intervals)))

    for i, expected in enumerate(arr):
        result = union_of_intervals(lower, upper, i)

        if result != expected:
            print(f"Fail: {result=}, {expected=}, {lower=}, {upper=}")
