n = int(input())

p = [0] + list(map(int, input().rstrip().split()))

for x in range(1, n + 1):
    print(p.index(p.index(x)))
