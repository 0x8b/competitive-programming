#!/bin/python3

import os


def compareTriplets(a, b):
    e = 0
    f = 0

    for [c, d] in zip(a, b):
        if c - d > 0:
            e += 1

        if c - d < 0:
            f += 1

    return [e, f]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
