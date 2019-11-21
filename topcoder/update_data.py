#!/usr/bin/env python

from operator import itemgetter
from pathlib import Path
import pyperclip
import requests
import json
import sys
import re

url = pyperclip.paste()

try:
    response = requests.get(url)
except:
    print(f"ERROR. URL: {url}")
    sys.exit(0)

problem_name = re.compile(r"Problem Statement for ([^<]+)", re.MULTILINE)
html = str(response.content)

if match := problem_name.search(html):
    name = match.group(1)

    with open("data.json", "r") as f:
        data = json.load(f)
        categories = sorted(data.keys())
        problem = {
            "name": name.strip(),
            "desc": url.strip(),
        }

        while True:
            print("\n".join(map(str, [f"{i}. {c}" for i, c in enumerate(categories)])))

            choice = int(input(f"[-1..{len(categories) - 1}]: "))

            if 0 <= choice < len(categories):
                data[categories[choice]].append(problem)
                break
            elif choice == -1:
                new_category = input("New category: ")
                data[new_category] = [problem]
                break

    with open("data.json", "w") as f:
        for key in data.keys():
            data[key].sort(key=itemgetter("name"))

        f.write(json.dumps(data, indent=4, sort_keys=True))

    Path(f'solutions/{name}.{input("Extension: ")}').touch()
else:
    print("Problem name not found.")
