n, k = map(int, input().split())

height = list(map(int, input().rstrip().split()))

a, m = 0, max(height)

if m > k:
    a = m - k

print(a)
