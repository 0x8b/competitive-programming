#!/bin/python3


import os


def flipping_bits(n):
    return ~n & 0xFFFFFFFF


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flipping_bits(n)

        fptr.write(str(result) + "\n")

    fptr.close()
