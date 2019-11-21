#!/bin/python3

import os


def quickSort(arr):
    left = []
    equal = [arr[0]]
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            equal.append(arr[i])

    return left + equal + right


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
