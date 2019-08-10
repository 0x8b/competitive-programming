nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

m = sum(bill)
w = m - bill[k]

if b - w // 2 == 0:
    print('Bon Appetit')
else:
    print(b - w // 2)
