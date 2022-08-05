from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

counter_cars = 0
cars_queue = deque()

command = input()
while not command == "END":
    crash = False
    total = green_light_duration + free_window_duration
    if not command == "green":
        cars_queue.append(command)
    else:
        while total - free_window_duration > 0 and cars_queue:
            current_car = cars_queue.popleft()
            if len(current_car) <= total:
                total -= len(current_car)
                counter_cars += 1

            elif len(current_car) > total:
                index = len(current_car) - total
                char = current_car[-index]
                crash = True
                print("A crash happened!")
                print(f"{current_car} was hit at {char}.")
                break
    if crash:
        break
    command = input()

if command == "END":
    print("Everyone is safe.")
    print(f"{counter_cars} total cars passed the crossroads.")
