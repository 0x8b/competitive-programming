#!/usr/bin/env python

"""
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

k, a = 17, [10, 15, 3, 7]


def one_pass(a, k):
    s = set()

    for i in a:
        if k - i in s:
            return True
        else:
            s.add(i)

    return False


print(one_pass(a, k))  # True


def two_sets(a, k):
    p = set(a) & set([k - i for i in a])  # intersection

    return len(p) > 0


print(two_sets(a, k))  # True
