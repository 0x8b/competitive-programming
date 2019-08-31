n, m = map(int, input().split())

counter = 0

image = [input() for _ in range(n)]

if n > 1 and m > 1:
    for y in range(n - 1):
        for x in range(m - 1):
            counter += set('face') == set(image[y][x:x+2] + image[y+1][x:x+2])

print(counter)
