n, k, x = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

result = sum(a[:len(a) - k]) + k * x

print(result)
