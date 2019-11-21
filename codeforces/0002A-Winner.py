from collections import defaultdict

n = int(input())
m = float("-inf")
winner = None
data = []
results = defaultdict(int)

for _ in range(n):
    name, score = input().split()
    score = int(score)
    results[name] += score
    data.append((name, score))

m = max(results.values())
names = [name for name, score in results.items() if score == m]
results = defaultdict(int)

for name, score in data:
    if name in names:
        results[name] += score

        if results[name] >= m:
            winner = name
            break

print(winner)
