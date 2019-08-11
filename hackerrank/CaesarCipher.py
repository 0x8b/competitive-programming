from string import ascii_lowercase as az

n = input()
s = input()
k = int(input()) % 26

r = az[k:] + az[:k]

trans = str.maketrans(az + az.upper(), r + r.upper())

print(s.translate(trans))
