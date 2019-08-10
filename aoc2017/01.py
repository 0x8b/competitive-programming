#!/usr/bin/env python

digits = input().strip()


def inverse_captcha(p):
    return sum(int(a) for a, b in zip(digits, digits[p:] + digits[:p]) if a == b)


assert inverse_captcha(1) == 995

half = len(digits) // 2

assert inverse_captcha(half) == 1130
