a = input().lower()
b = input().lower()

print(0 if a == b else 2 * (a > b) - 1)
