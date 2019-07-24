q = int(input())

for _ in range(q):
    a, b, c = map(int, input().strip().split())

    s = a + b + c

    print(s // 2)
