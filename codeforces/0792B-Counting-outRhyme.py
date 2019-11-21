n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

ch = list(range(1, n + 1))

curr = 0
out = []

for i in range(k):
    curr = (curr + a[i]) % len(ch)

    out.append(ch.pop(curr))

    if curr == len(ch):
        curr = 0

print(" ".join(map(str, out)))
