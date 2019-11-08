n = int(input())
a = sorted(list(map(int, input().rstrip().split())))

diff = [abs(a - b) for a, b in zip(a, a[1:])]

print(min(diff))
