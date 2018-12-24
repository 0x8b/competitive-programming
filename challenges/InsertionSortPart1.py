#!/bin/python3

import os


def insertionSort1(n, arr):
    el = arr[-1]

    for i in reversed(range(1, n)):
        if arr[i - 1] > el:
            arr[i] = arr[i - 1]
            print(" ".join(map(str, arr)))
        else:
            arr[i] = el
            print(" ".join(map(str, arr)))
            return
        
    arr[0] = el
    print(" ".join(map(str, arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
