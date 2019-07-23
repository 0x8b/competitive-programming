n = int(input())

ans = (n * (n + 1)) // 2
ans = 4 * ans
ans = ans - 4 * n
ans = 1 + ans

print(ans)
