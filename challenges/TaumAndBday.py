t = int(input())

for _ in range(t):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())

    bc = min(bc, wc + z)
    wc = min(wc, bc + z)

    print(b * bc + w * wc)
