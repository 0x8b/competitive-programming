#!/bin/python3

import os
import sys


def grading_policy(g):
    if g >= 38 and (5 - g % 5) < 3:
        return g - (g % 5) + 5

    return g


def grading_students(grades):
    return map(lambda x: grading_policy(x), grades)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = grading_students(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
