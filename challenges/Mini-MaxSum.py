#!/bin/python3

import math
import os

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max = 0
    min = math.inf

    for num in arr:
        s = sum(arr) - num

        if s > max:
            max = s
        
        if s < min:
            min = s
    
    return min, max

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    min, max = miniMaxSum(arr)

    print(min, max)
