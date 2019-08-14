for _ in range(int(input())):
    n = int(input())

    sticks = list(map(int, input().strip().split()))
    sticks.sort()

    areas = []
    eq = []

    for _ in range(n):
        a, b, *sticks, c, d = sticks

        eq.append(a == b and c == d)
        areas.append(a * c)

    print('YES' if all(eq) and all(areas[0] == a for a in areas) else 'NO')
