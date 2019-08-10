import re

n = int(input())
b = input()

print(len(re.findall(r"010", b)))
