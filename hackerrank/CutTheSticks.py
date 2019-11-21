n = int(input())
arr = list(map(int, input().rstrip().split()))

while len(arr) > 0:
    print(len(arr))

    m = min(arr)

    arr = [x - m for x in arr if x - m > 0]
