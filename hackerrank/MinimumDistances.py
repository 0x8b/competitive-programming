n = int(input())
a = list(map(int, input().rstrip().split()))

distances = []

for number in set(a):
    if a.count(number) > 1:
        delta = a[a.index(number) + 1:].index(number) + 1
        distances.append(delta)

result = -1

if distances:
    result = min(distances)

print(result)
