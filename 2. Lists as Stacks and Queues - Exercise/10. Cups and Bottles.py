from collections import deque

cup_capacity = deque([int(el) for el in input().split()])
bottle_with_water = [int(el) for el in input().split()]

wasted_water = 0

while cup_capacity and bottle_with_water:
    current_bottle = bottle_with_water.pop()
    current_cup = cup_capacity.popleft()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    elif current_bottle < current_cup:
        cup_capacity.appendleft(current_cup - current_bottle)

if not cup_capacity:
    print(f"Bottles: {' '.join([str(el) for el in bottle_with_water])}")
if not bottle_with_water:
    print(f"Cups: {' '.join([str(el) for el in cup_capacity])}")
print(f"Wasted litters of water: {wasted_water}")