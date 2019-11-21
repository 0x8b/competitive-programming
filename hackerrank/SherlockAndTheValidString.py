from collections import Counter

c = sorted(Counter(input()).values())

if len(set(c)) == 1:
    print("YES")
elif c[0] == 1 and len(set(c[1:])) == 1:
    print("YES")
elif c[0] + 1 == c[-1] and len(set(c[:-1])) == 1:
    print("YES")
else:
    print("NO")
