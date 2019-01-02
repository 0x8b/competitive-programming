t = int(input())

i = 0
a = 0

while a < t:
    a += 3 * 2 ** i
    i += 1

value = 3 * 2 ** (i - 1)

time = value - 2

s = value - (t - time)

print(s)
