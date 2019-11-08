t = int(input())

for _ in range(t):
    n = int(input())

    i = 1

    while True:
        b = int(bin(i)[2:]) * 9  # [2:] - remove leading 0b

        i += 1

        if b % n == 0:
            print(b)
            break
