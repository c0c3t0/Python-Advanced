def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

field = []
alice_row = 0
alice_col = 0
rabbit_row = 0
rabbit_col = 0

for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == "A":
            alice_row, alice_col = row, col
            field[row][col] = "*"
        if field[row][col] == "R":
            rabbit_row, rabbit_col = row, col

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

collected = 0
out = False

while not alice_row == rabbit_row or not alice_col == rabbit_col:
    command = input()
    current_row, current_col = alice_row, alice_col
    for direction, step in directions.items():
        if command == direction:
            next_move_row, next_move_col = step(current_row, current_col)
            if not is_valid_position(size, next_move_row, next_move_col):
                out = True
                break
            if field[next_move_row][next_move_col].isdigit():
                collected += int(field[next_move_row][next_move_col])
            field[next_move_row][next_move_col] = "*"
            alice_row, alice_col = next_move_row, next_move_col
    if collected >= 10:
        break
    if out:
        break

if out or (alice_row == rabbit_row and alice_col == rabbit_col):
    print("Alice didn't make it to the tea party.")
elif collected >= 10:
    print("She did it! She went to the party.")
for row_elements in field:
    print(' '.join(row_elements))
