n = int(input())

x = list(map(lambda a: int(a) % 2, input().split()))

odd = x.count(1)

print(min(odd, len(x) - odd))
