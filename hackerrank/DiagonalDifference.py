def diagonal_difference(a):
    return abs(sum(a[i][i] - a[i][n - 1 - i] for i in range(n)))


n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(diagonal_difference(arr))
