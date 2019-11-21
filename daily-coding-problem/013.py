#!/usr/bin/env python

"""
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""


def longest_substring(s, k):
    maximum_substring_length = 0
    last_position = dict()
    chars = set()
    sliding_window_start = 0
    sliding_window_end = 0

    for i, c in enumerate(s):
        sliding_window_end = i
        last_position[c] = i

        chars.add(c)

        if len(chars) > k:
            min_position = min(last_position.values())

            for c, p in last_position.items():
                if p == min_position:
                    chars.remove(c)
                    del last_position[c]
                    sliding_window_start = p + 1
                    break

        maximum_substring_length = max(
            maximum_substring_length, sliding_window_end - sliding_window_start + 1
        )

    return maximum_substring_length


print(longest_substring("abcba", 2))  # 3
