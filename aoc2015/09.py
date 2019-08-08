#!/usr/bin/env python

import re
import fileinput

sep = re.compile(r' to | = ')

data = [sep.split(line.strip()) for line in fileinput.input()]

print(data)
