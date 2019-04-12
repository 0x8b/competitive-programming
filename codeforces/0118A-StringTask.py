#! python

s = input()

print(''.join(['.' + c for c in s.lower() if c not in 'aoyeui']))
