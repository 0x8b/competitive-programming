s = list(input().strip())

q = int(input())

for _ in range(q):
    mode, posl, cr = input().strip().split()

    if int(mode) == 2:
        cr = int(cr)
        print(len(set(s[int(posl) - 1 : cr])))
    else:
        i = int(posl) - 1
        s[i] = cr
