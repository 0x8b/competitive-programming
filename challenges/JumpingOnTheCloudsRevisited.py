from itertools import count, takewhile

n, k = map(int, input().split())

c = list(map(int, input().rstrip().split()))

g = (i % n for i in count(k, k))

visited_clouds = [c[i] for i in takewhile(lambda x: x != 0, g)] + [c[0]]

e = 100 - 2 * sum(visited_clouds) - len(visited_clouds)

print(e)
