n = int(input())
password = input()

a = 4
s = set(password)

a -= bool(s & set("0123456789"))
a -= bool(s & set("abcdefghijklmnopqrstuvwxyz"))
a -= bool(s & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
a -= bool(s & set("!@#$%^&*()-+"))

print(a if n + a >= 6 else 6 - n)
