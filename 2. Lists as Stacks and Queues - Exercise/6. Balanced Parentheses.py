sequence = input()

stack = []
mirrors = {"(": ")", "{": "}", "[": "]"}
balanced = True


for parentheses in sequence:
    if parentheses not in "({[" and not stack:
        balanced = False
        break
    if parentheses in "({[":
        stack.append(parentheses)
    else:
        if not mirrors[stack.pop()] == parentheses:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")