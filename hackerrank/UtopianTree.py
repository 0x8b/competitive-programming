t = int(input())

for i in range(t):
    n = int(input())

    h = 1

    for j in range(n):
        if j & 1:
            h += 1
        else:
            h *= 2
    
    print(h)
