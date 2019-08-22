#!/usr/bin/env python

import re
import fileinput

from collections import defaultdict, Counter
from operator import itemgetter

c = re.compile(r'(\w+)')

values = {}
children = defaultdict(list)

lines = [line for line in fileinput.input()]

head = Counter(re.compile(r'([a-z]+)').findall('\n'.join(lines))).most_common()[-1][0]

assert head == 'cqmvs'


def parse(line):
    name, weight, *ch = c.findall(line)

    values[name] = int(weight)
    children[name] = ch


data = [parse(line) for line in lines]

ans = None


def t(name):
    global ans

    if children[name]:
        v, s = zip(*[(values[n], t(n)) for n in children[name]])

        if len(set(s)) > 1:
            mc = list(map(itemgetter(0), Counter(s).most_common()))

            diff = mc[-1] - mc[0]

            if not ans:
                ans = v[s.index(mc[-1])] - diff

        return values[name] + sum(s)
    else:
        return values[name]


t(head)

assert ans == 2310
