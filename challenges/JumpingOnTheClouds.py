n = int(input())
c = list(map(int, input().rstrip().split()))

i = 0

a = 0

while i < n - 2:
    if c[i + 2] == 0:
        i += 2
    else:
        i += 1

    a += 1

if i == n - 2:
    a += 1

print(a)
