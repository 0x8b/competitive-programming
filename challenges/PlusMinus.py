#!/bin/python3

import os

# Complete the plusMinus function below.
def plusMinus(arr):
    l = len(arr)
    p = n = z = 0

    for i in arr:
        if i < 0:
            n += 1
        elif i > 0:
            p += 1
        else:
            z += 1

    return map(lambda x: '{0:.6f}'.format(x / l), [p, n, z])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)

    print('\n'.join(result))
