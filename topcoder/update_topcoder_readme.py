#!/usr/bin/env python

from pathlib import Path
from operator import itemgetter
import json


with open("data.json", "r") as f:
    data = json.load(f)

links = {
    problem["name"]: problem["desc"]
    for problems in data.values()
    for problem in problems
}

languages = {
    "py": "Python",
    "rs": "Rust",
}

with open("README.md", "w", encoding="utf8") as readme:
    readme.write("# TopCoder\n\n")

    for category in sorted(data.keys()):
        readme.write(f"### {category}\n\n")
        readme.write(f"|Name|Solution|Description|\n")
        readme.write(f"|---|---|---|\n")

        for problem in sorted(data[category], key=itemgetter("name")):
            name = problem["name"]
            solutions = Path("solutions")

            for path in solutions.glob(f"{name}.*"):
                line = [
                    name,
                    f"[{languages[path.suffix[1:]]}](/topcoder/solutions/{path.name})",
                    f'<a href="{problem["desc"]}" target="_blank">TopCoder \U0001F855</a>',
                ]

                readme.write(f'|{"|".join(map(str, line))}|\n')
