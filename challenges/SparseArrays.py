from collections import Counter

strings = [input() for _ in range(int(input()))]
queries = [input() for _ in range(int(input()))]

c = Counter(strings)

for q in queries:
    print(c[q] if q in c else 0)
