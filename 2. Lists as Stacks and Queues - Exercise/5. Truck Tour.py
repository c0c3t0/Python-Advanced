from collections import deque

n = int(input())

stations = deque()

for num in range(n):
    stations.append([el for el in input().split()])

for index_stations in range(n):
    is_valid = True
    tank_petrol = 0
    for station in range(n):
        tank_petrol += int(stations[station][0]) - int(stations[station][1])
        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    if is_valid:
        print(index_stations)
        break

