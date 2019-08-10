#!/bin/python3

import os


def diagonalDifference(arr):
    result = 0

    for i in range(n):
        result += arr[i][i] - arr[i][n - 1 - i]

    return abs(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
