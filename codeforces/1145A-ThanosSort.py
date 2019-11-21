n = int(input())

arr = list(map(int, input().split()))


def check(a):
    length = len(a)

    if a == sorted(a):
        return length

    p = length // 2

    return max(check(a[:p]), check(a[p:]))


print(check(arr))
