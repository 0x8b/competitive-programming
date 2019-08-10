#!/bin/python3


import os


def breakingRecords(scores):
    h = 0
    l = 0

    min_score = scores[0]
    max_score = scores[0]

    for s in scores[1:]:
        if s > max_score:
            max_score = s
            h += 1
        
        if s < min_score:
            min_score = s
            l += 1

    return h, l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
