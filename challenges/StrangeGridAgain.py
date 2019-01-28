r, c = map(int, input().split())

a = ((r - 1) // 2 * 10) + (c * 2 - 1 if r % 2 == 0 else (c - 1) * 2)

print(a)
