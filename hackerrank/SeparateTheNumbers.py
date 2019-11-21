q = int(input())

for _ in range(q):
    s = input()

    if len(s) > 1:
        for i in range(1, len(s) // 2 + 1):
            first, rest = int(s[:i]), s[i:]
            n = first

            while rest:
                n = str(n + 1)

                if rest.startswith(n):
                    rest = rest[len(str(n)) :]

                else:
                    break

                n = int(n)

            if rest == "":
                print("YES", first)
                break

            elif i == len(s) // 2:
                print("NO")

    else:
        print("NO")
