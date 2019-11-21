n, d = map(int, input().split())

a = list(input().rstrip().split())

a = a[d:] + a[:d]

print(" ".join(a))
