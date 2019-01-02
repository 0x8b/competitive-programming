import itertools

n, d = map(int, input().split())

arr = list(map(int, input().rstrip().split()))

counter = 0

for i in range(0, n - 2):
    subsequence = list(itertools.takewhile(lambda x: x - arr[i] <= 2 * d, arr[i:]))

    if len(subsequence) > 2:
        # set, otherwise: 3x(7 10 13) in 1 6 7 7 8 10 12 13 14 19 sequence
        for ai, aj, ak in set(itertools.combinations(subsequence, 3)):
            if aj - ai == d and ak - aj == d:
                counter += 1

print(counter)
