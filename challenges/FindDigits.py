for _ in range(int(input())):
    n = input()
    c = 0

    for digit in n:
        p = int(digit)

        if p != 0 and int(n) % p == 0:
            c += 1

    print(c)
