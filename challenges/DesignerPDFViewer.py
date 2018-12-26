h = list(map(int, input().rstrip().split()))

word = set(input())

tallest = 0

for letter in set(word):
    height = h[ord(letter) - ord('a')]

    tallest = max(height, tallest)

result = tallest * len(word)

print(result)
