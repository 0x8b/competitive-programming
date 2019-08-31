l, r = input().split()


def count(s: str) -> int:
    if s[0] != s[-1]:
        while s[0] != s[-1]:
            s = str(int(s) - 1)

    length = len(s)
    cnt = 0

    if length == 1:
        return int(s)

    if length == 2:
        return 9 + int(s[0])

    # length > 2
    cnt += 9  # 1 2 ... 9
    cnt += 9  # 11 22 ... 99
    cnt += 1 + int(s[1:-1])  # _x..._
    cnt += (int(s[0]) - 1) * 10 ** (length - 2)
    cnt += sum(9 * 10 ** (n - 2) for n in range(3, length))

    return cnt


print((l[0] != l[-1]) * -1 + count(r) - count(l) + 1)

