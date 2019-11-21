n = int(input())

x, y = list(zip(*[tuple(input().split()) for _ in range(n)]))

x = all(x[0] == a for a in x)
y = all(y[0] == a for a in y)

print("YES" if x or y else "NO")
