t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().rstrip().split()))

    print("YES" if sum(x <= 0 for x in a) < k else "NO")
