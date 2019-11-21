q = int(input())

for _ in range(q):
    n = int(input())
    reachable = True

    path = zip(map(int, list(input().strip())), map(int, list(input().strip())))

    level = False  # top

    for step in path:
        if step[level] in {1, 2}:
            pass
        elif not set(step).intersection({1, 2}):
            level = not level
        else:
            reachable = False
            break

    print("YES" if reachable and level else "NO")
