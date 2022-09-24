from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:
    effect = firework_effects.popleft()
    explosive = explosive_power.pop()
    if effect <= 0:
        explosive_power.append(explosive)
        continue
    if explosive <= 0:
        firework_effects.appendleft(effect)
        continue
    sum_firework = effect + explosive
    if sum_firework % 3 == 0 and sum_firework % 5 == 0:
        crossette_firework += 1
    elif sum_firework % 5 == 0 and not sum_firework % 3 == 0:
        willow_firework += 1
    elif sum_firework % 3 == 0 and not sum_firework % 5 == 0:
        palm_firework += 1
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(explosive)
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
print(
    f"Palm Fireworks: {palm_firework}\nWillow Fireworks: {willow_firework}\nCrossette Fireworks: {crossette_firework}")
