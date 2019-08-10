n = int(input().strip())

a = sorted(list(map(int, input().rstrip().split())))

m = 0

for i in range(0, n):
    c = a[i]
    k = 0

    for j in range(i, n):
        if a[j] - c < 2:
            k += 1

            if k > m:
                m = k
        else:
            break

print(m)
