s = input()
n = int(input())

a = s.count('a')

r = n % len(s)

print(n // len(s) * a + s[:r].count('a'))