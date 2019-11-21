for _ in range(int(input())):
    s = sorted(input())

    print(("no", "yes")[len(s) == len(set(s)) == (1 + ord(s[-1]) - ord(s[0]))])
