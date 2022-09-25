from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casing = [int(el) for el in input().split(", ")]

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

bomb_sum = 0
succeed = False

while bomb_effects and bomb_casing:
    bomb = bomb_effects.popleft()
    casing = bomb_casing.pop()
    bomb_sum = bomb + casing
    if bomb_sum == 40:
        datura_bombs += 1
    elif bomb_sum == 60:
        cherry_bombs += 1
    elif bomb_sum == 120:
        smoke_decoy_bombs += 1
    else:
        bomb_effects.appendleft(bomb)
        bomb_casing.append(casing - 5)
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        succeed = True
        break

if succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}\nDatura Bombs: {datura_bombs}\nSmoke Decoy Bombs: {smoke_decoy_bombs}")
