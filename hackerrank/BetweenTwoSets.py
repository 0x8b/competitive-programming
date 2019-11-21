#!/bin/python3

import os


def getTotalX(a, b):
    c = 0

    for i in range(max(a), min(b) + 1):
        if all([i % d == 0 for d in a]) and all([d % i == 0 for d in b]):
            c += 1

    return c


if __name__ == "__main__":
    f = open(os.environ["OUTPUT_PATH"], "w")

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + "\n")

    f.close()
