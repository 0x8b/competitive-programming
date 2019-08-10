n, m = map(int, input().split())

stations = list(map(int, input().rstrip().split()))

max_distance = 0

for city in range(n):
    distances = []

    for station in stations:
        distances.append(abs(city - station))

    max_distance = max(max_distance, min(distances))

print(max_distance)
