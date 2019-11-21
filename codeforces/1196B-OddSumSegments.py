from itertools import compress, count

q = int(input())

for _ in range(q):
    n, k = map(int, input().strip().split())

    a = input().strip().split()

    parity = [int(e) % 2 for e in a]
    odd = sum(parity)

    if odd >= k and ((odd - k) % 2) == 0:
        print("YES")
        print(" ".join(map(str, (list(compress(count(1), parity))[:-1] + [n])[-k:])))

    else:
        print("NO")
