n, k, q = map(int, input().split())

a = list(map(int, input().rstrip().split()))

k = k % n

a = a[n - k :] + a[: n - k]

for _ in range(q):
    m = int(input())

    print(a[m])
