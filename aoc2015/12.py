#!/usr/bin/env python

import re
import json

content = input()

number = re.compile(r'-?\d+')

all_numbers = map(int, number.findall(content))

parsed = json.loads(content)


def traverse(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, dict) and 'red' in v.values():
                node[k] = 0

            traverse(node[k])
    elif isinstance(node, list):
        for i in range(len(node)):
            if isinstance(node[i], dict) and 'red' in node[i].values():
                node[i] = 0

            traverse(node[i])
    else:
        return


traverse(parsed)

assert sum(all_numbers) == 119433

content = json.dumps(parsed, indent=4, sort_keys=True)

assert sum(map(int, number.findall(content))) == 68466
