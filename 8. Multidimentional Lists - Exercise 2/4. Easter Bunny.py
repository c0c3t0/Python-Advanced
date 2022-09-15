import sys

def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

field = []
bunny_row, bunny_col = 0, 0
max_eggs = -sys.maxsize
best_direction = ''
best_path = []

for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == "B":
            bunny_row, bunny_col = row, col
            break

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1)
}


for direction, step in directions.items():
    eggs = 0
    path = []
    current_row, current_col = bunny_row, bunny_col
    while is_valid_position(size, current_row, current_col):
        current_row, current_col = step(current_row, current_col)
        if not is_valid_position(size, current_row, current_col):
            break
        if field[current_row][current_col] == "X":
            break
        else:
            path.append([current_row, current_col])
            eggs += int(field[current_row][current_col])
        if max_eggs < eggs:
            best_direction, best_path, max_eggs = direction, path, eggs

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
