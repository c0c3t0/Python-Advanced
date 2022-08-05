string = input().split()

reversed_string = []
while string:
    reversed_string.append(string.pop())

print(*reversed_string)