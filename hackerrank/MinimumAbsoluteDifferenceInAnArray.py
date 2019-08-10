n = int(input())

arr = sorted(list(map(int, input().rstrip().split())))

diff = [abs(a - b) for a, b in zip(arr, arr[1:])]

print(min(diff))
