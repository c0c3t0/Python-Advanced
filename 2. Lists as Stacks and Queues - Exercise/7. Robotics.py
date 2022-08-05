from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")
starting_time = datetime.strptime(input(), '%H:%M:%S')

for el in range(len(robots)):
    info = robots[el].split("-")
    robots[el] = {'name': info[0], 'processing_time': int(info[1]), 'available_at': 0}

product = input()
products = deque()
while not product == "End":
    products.append(product)
    product = input()

current_time = 0
while products:
    current_time += 1
    current_product = products.popleft()
    for robot in robots:
        if robot['available_at'] <= current_time:
            robot['available_at'] = current_time + robot['processing_time']
            output_time = (starting_time + timedelta(seconds=current_time)).strftime('%H:%M:%S')
            print(f"{robot['name']} - {current_product} [{output_time}]")
            break
    else:
        products.append(current_product)