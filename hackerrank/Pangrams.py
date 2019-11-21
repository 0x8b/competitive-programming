s = input().strip().replace(" ", "").lower()

if len(set(s)) == 26:
    print("pangram")
else:
    print("not pangram")
