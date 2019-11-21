from functools import cmp_to_key

n = int(input())

unsorted = []

for _ in range(n):
    unsorted.append(input())


def custom(a, b):
    if len(a) == len(b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    else:
        return len(a) - len(b)


unsorted.sort(key=cmp_to_key(custom))

for number in unsorted:
    print(number)
