t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().strip().split())

    cnt = 0

    while n:
        if k > n:
            cnt += n
            n = 0
        elif n % k:
            n -= 1
            cnt += 1
        else:
            n = n // k
            cnt += 1

    print(cnt)
