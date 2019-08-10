arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

freq = [0] * 6

for i in range(len(arr)):
    freq[arr[i]] += 1

print(freq.index(max(freq)))
