commands = int(input())

cars = set()
for i in range(commands):
    direction, car_plate = input().split(", ")
    if direction == "IN":
        cars.add(car_plate)
    elif direction == "OUT":
        cars.discard(car_plate)

if not cars:
    print("Parking Lot is Empty")
else:
    print('\n'.join(cars))