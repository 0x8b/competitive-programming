h = list(map(int, input().rstrip().split()))

word = input()

h = [h[ord(l) - ord('a')] for l in set(word)]

print(max(h) * len(word))
