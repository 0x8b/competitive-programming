n = int(input())

arr = list(map(int, input().rstrip().split()))

counter = [0] * 101

for e in arr:
    counter[e] += 1

print(n - max(counter))
