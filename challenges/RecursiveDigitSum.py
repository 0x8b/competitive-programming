n, k = input().split()

k = int(k)

n = k * sum(map(int, list(n)))

while n > 9:
    n = sum(map(int, list(str(n))))

print(n)
