n = int(input())
s = list(input())
k = int(input())

k = k % 26

for i, letter in enumerate(s):
    if letter.isalpha():
        case = 'a' if letter.islower() else 'A'

        s[i] = chr(ord(case) + (ord(letter) + k) % ord(case) % 26)

print(''.join(s))
