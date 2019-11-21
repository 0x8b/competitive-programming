import re

s = input()

p = re.compile(r"(\w)\1")

while re.search(p, s):
    s = re.sub(p, "", s)

print("Empty String" if len(s) == 0 else s)
