def is_inside(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == "up":
        return r - 1, c
    elif direction == "down":
        return r + 1, c
    elif direction == "left":
        return r, c - 1
    elif direction == "right":
        return r, c + 1


size = int(input())

field = []
snake_row = 0
snake_col = 0
burrows = []

for row in range(size):
    field.append(list(input()))
    for col in range(size):
        if field[row][col] == "S":
            field[row][col] = '.'
            snake_row, snake_col = row, col
        if field[row][col] == "B":
            burrows.append([row, col])

food = 0
outside = False

while True:
    command = input()
    next_row, next_col = get_next_position(command, snake_row, snake_col)
    if not is_inside(size, next_row, next_col):
        outside = True
        print("Game over!")
        break
    if field[next_row][next_col] == "*":
        field[next_row][next_col] = '.'
        food += 1
    if burrows and field[next_row][next_col] == "B":
        if next_row == burrows[0][0] and next_col == burrows[0][1]:
            field[next_row][next_col] = '.'
            next_row = burrows[1][0]
            next_col = burrows[1][1]
        elif next_row == burrows[1][0] and next_col == burrows[1][1]:
            field[next_row][next_col] = '.'
            next_row = burrows[0][0]
            next_col = burrows[0][1]
    field[next_row][next_col] = '.'
    snake_row, snake_col = next_row, next_col
    if food == 10:
        print("You won! You fed the snake.")
        break

if not outside:
    field[snake_row][snake_col] = "S"

print(f"Food eaten: {food}")
for row_elements in field:
    print(''.join(row_elements))