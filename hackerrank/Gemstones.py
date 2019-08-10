n = int(input())

arr = []

for _ in range(n):
    arr.append(set(input()))

    arr[0] = arr[0] & arr[-1]

print(len(arr[0]))

# alternative
rocks = [set(input()) for _ in range(int(input()))]

print(len(set.intersection(*rocks)))
