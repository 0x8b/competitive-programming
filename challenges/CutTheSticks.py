n = int(input())
arr = list(map(int, input().rstrip().split()))

while len(arr) > 0:
    print(len(arr))

    m = min(arr)

    for i in range(len(arr)):
        arr[i] -= m

    arr = list(filter(lambda x: x > 0, arr))
