from itertools import product


def transform(c):
    return c == "*"


def argmax_all(a):
    sum_of_row = [sum(b) for b in a]

    m = max(sum_of_row)

    return m, [i for i, v in enumerate(sum_of_row) if v == m]


q = int(input())

for _ in range(q):
    n, m = map(int, input().strip().split())

    a = []

    for _ in range(n):
        a.append(list(map(transform, list(input().strip()))))

    max_row, row_indexes = argmax_all(a)
    max_col, col_indexes = argmax_all(zip(*a))

    ans = n - max_col + m - max_row

    for r, c in product(row_indexes, col_indexes):
        if not a[r][c]:
            ans -= 1
            break

    print(ans)
