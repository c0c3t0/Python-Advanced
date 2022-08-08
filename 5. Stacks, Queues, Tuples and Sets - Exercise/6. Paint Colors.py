from collections import deque

text = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

crafted_colors = []
while text:
    left = text.popleft()
    right = text.pop() if text else ''
    var_1 = left + right
    var_2 = right + left
    if var_1 in main_colors or var_1 in secondary_colors:
        crafted_colors.append(var_1)
    elif var_2 in main_colors or var_2 in secondary_colors:
        crafted_colors.append(var_2)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            text.insert(len(text) // 2, left)
        if right:
            text.insert(len(text) // 2, right)

if 'orange' in crafted_colors and ('red' not in crafted_colors or 'yellow' not in crafted_colors):
    crafted_colors.pop(crafted_colors.index('orange'))
if 'purple' in crafted_colors and ('red' not in crafted_colors or 'blue' not in crafted_colors):
    crafted_colors.pop(crafted_colors.index('purple'))
if 'green' in crafted_colors and ('blue' not in crafted_colors or 'yellow' not in crafted_colors):
    crafted_colors.pop(crafted_colors.index('green'))

print(crafted_colors)
