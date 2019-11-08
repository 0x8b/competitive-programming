s = input()
c = 0

for i in range(len(s) // 3):
    c += s[3 * i] != 'S'
    c += s[3 * i + 1] != 'O'
    c += s[3 * i + 2] != 'S'

print(c)
