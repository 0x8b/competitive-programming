n = int(input())
a = list(map(int, input().rstrip().split()))

unique = 0

for i in a:
    unique ^= i

print(unique)
