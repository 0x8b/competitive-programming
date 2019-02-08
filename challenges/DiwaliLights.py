for i in range(int(input())):
    a = 1

    for j in range(int(input())):
        a *= 2
        a %= 100000

    print(a - 1)
