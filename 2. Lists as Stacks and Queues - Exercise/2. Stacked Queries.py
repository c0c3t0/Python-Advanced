n = int(input())

stack = []
for lines in range(n):
    query = input()
    if query.startswith("1"):
        num = query.split()[-1]
        stack.append(int(num))
    elif stack:
        if query == "2":
            stack.pop()
        elif query == "3":
            print(max(stack))
        elif query == "4":
            print(min(stack))

stack_of_str = [str(el) for el in stack]
print(', '.join(stack_of_str[::-1]))
