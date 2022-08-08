from collections import deque

working_bees = deque(int(el) for el in input().split())
all_nectar = [int(el) for el in input().split()]
symbols = deque(input().split())

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
total_honey = 0

while working_bees and all_nectar:
    bee = working_bees.popleft()
    nectar = all_nectar.pop()

    if bee <= nectar:
        current_symbol = symbols.popleft()
        if not nectar == 0:
            total_honey += abs(operations[current_symbol](bee, nectar))
    else:
        working_bees.appendleft(bee)
print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if all_nectar:
    print(f"Nectar left: {', '.join([str(x) for x in all_nectar])}")
