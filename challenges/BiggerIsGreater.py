t = int(input())

for _ in range(t):
    w = list(input())

    i = len(w) - 1

    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:
        print('no answer')
        continue

    k = len(w) - 1

    while w[k] <= w[i - 1]:
        k -= 1

    w[i - 1], w[k] = w[k], w[i - 1]

    w[i:] = w[len(w) - 1 : i - 1 : -1]

    print(''.join(w))
