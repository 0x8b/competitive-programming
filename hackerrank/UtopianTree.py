t = int(input())

for i in range(t):
    n = int(input())

    h = 1

    for i in range(n):
        if i & 1:
            h += 1
        else:
            h *= 2
    
    print(h)
