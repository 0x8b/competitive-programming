s = input()
n = int(input())

a = s.count('a')

q, r = divmod(n, len(s))

print(q * a + s[:r].count('a'))
