#!/bin/python3

import itertools
import os


def maximizingXor(l, r):
    return max(map(lambda x: x[0] ^ x[1], itertools.combinations(range(l, r + 1), 2)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
