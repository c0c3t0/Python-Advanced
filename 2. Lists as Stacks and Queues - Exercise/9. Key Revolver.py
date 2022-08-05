from collections import deque

price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
value_of_intelligence = int(input())

counter = size_of_gun_barrel
shots = 0
while bullets or locks:
    if not bullets or not locks:
        break
    bullet = bullets.pop()
    counter -= 1
    shots += 1
    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if counter == 0 and bullets:
        counter = size_of_gun_barrel
        print("Reloading!")

money = value_of_intelligence - (shots * price_of_bullet)
if not bullets and locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif not locks:
    print(f"{len(bullets)} bullets left. Earned ${money}")
