from collections import deque

expression = input().split()
numbers = deque()

for symbol in expression:
    if symbol.isdigit() or len(symbol) > 1:
        numbers.append(int(symbol))
    else:
        while len(numbers) > 1:
            if symbol == "*":
                numbers.appendleft(int(f"{numbers.popleft() * numbers.popleft()}"))
            elif symbol == "+":
                numbers.appendleft(int(f"{numbers.popleft() + numbers.popleft()}"))
            elif symbol == "-":
                numbers.appendleft(int(f"{numbers.popleft() - numbers.popleft()}"))
            elif symbol == "/":
                numbers.appendleft(int(f"{numbers.popleft() // numbers.popleft()}"))

print(*numbers)
