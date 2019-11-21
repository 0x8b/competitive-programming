#!/usr/bin/env python

"""
Given the root to a binary search tree, find the second largest node
in the tree.
"""

from collections import namedtuple

Node = namedtuple("Node", ["v", "l", "r"])


a = Node(1, None, None)
b = Node(0, None, None)
c = Node(0, None, None)
d = Node(6, None, None)
e = Node(5, None, None)
f = Node(4, None, None)
g = Node(4, None, None)
h = Node(7, None, None)

i = Node(5, a, b)
j = Node(2, c, d)
k = Node(8, e, f)
l = Node(3, g, h)

m = Node(1, i, j)
n = Node(2, k, l)

tree = Node(2, m, n)


largest = float("-inf")
second_largest = float("-inf")


def find_second_largest(node: Node):
    global largest, second_largest

    if node.v > largest:
        second_largest = largest
        largest = node.v
    elif node.v > second_largest:
        second_largest = node.v

    if node.l:
        find_second_largest(node.l)

    if node.r:
        find_second_largest(node.r)


find_second_largest(tree)


print(second_largest)
