from collections import defaultdict, Counter

n = int(input())
s = input().strip()
m = int(input())

positions = defaultdict(list)

for (index, letter) in enumerate(s):
    positions[letter].append(index)

for _ in range(m):
    c = Counter(input().strip())

    farthest = 0

    for (key, value) in c.items():
        farthest = max(farthest, positions[key][value - 1])

    print(farthest + 1)
