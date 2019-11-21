#!/bin/python3

import os
import sys


def timeConversion(s):
    hour = int(s[:2])

    if s.endswith("AM"):
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    hour = str(hour)

    if len(hour) == 1:
        hour = "0" + hour

    return hour + s[2:-2]


if __name__ == "__main__":
    f = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    f.write(result + "\n")

    f.close()
