#!/usr/bin/env python

import fileinput
import re

sep = re.compile(r" to | = ")

data = [sep.split(line.strip()) for line in fileinput.input()]

print(data)
