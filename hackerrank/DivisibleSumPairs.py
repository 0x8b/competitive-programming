import os
import itertools


def divisible_sum_pairs(n, k, ar):
    return len(
        list(filter(lambda x: (x[0] + x[1]) % k == 0, itertools.combinations(ar, 2)))
    )


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
