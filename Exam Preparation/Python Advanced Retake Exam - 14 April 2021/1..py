from collections import deque

orders = deque([int(el) for el in input().split(", ")])
capacities = [int(el) for el in input().split(", ")]

count = 0

while orders and capacities:
    pizza = orders.popleft()
    employee = capacities.pop()
    if pizza <= 0 or pizza > 10:
        capacities.append(employee)
        continue
    if pizza < employee:
        count += pizza
    elif pizza >= employee:
        count += employee
        orders.appendleft(pizza - employee)

if not orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {count}\nEmployees: {', '.join([str(x) for x in capacities])}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(x) for x in orders])}")
