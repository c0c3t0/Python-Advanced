from collections import deque

chocolates = [int(el) for el in input().split(", ")]
milk_cups = deque([int(el) for el in input().split(", ")])

count = 0

while chocolates and milk_cups and count < 5:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        count += 1
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!" if count == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolates])}" if chocolates else "Chocolate: empty")
print(f"Milk: {', '.join([str(x) for x in milk_cups])}" if milk_cups else "Milk: empty")
