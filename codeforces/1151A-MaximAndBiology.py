n = int(input())
s = input()

minumum = float("inf")

for i in range(n - 4 + 1):
    total = 0

    for a, b in zip("ACTG", s[i : i + 4]):
        distance = abs(ord(a) - ord(b))
        total += min(distance, 26 - distance)

    minumum = min(minumum, total)

print(minumum)
