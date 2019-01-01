t = int(input())

for t_itr in range(t):
    n = int(input())
    c = 0

    for digit in list(str(n)):
        p = int(digit)

        if p != 0 and n % p == 0:
            c += 1
    
    print(c)
