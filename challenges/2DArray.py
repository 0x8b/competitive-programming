arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

a = []

for x in range(0, 4):
    for y in range(0, 4):
        s = 0

        for mx in range(0, 3):
            for my in range(0, 3):
                s += arr[y + my][x + mx]

        s -= arr[y + 1][x]
        s -= arr[y + 1][x + 2]

        a.append(s)

print(max(a))
