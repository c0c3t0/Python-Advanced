def is_valid_position(r, c, size):
    return 0 <= r < size and 0 <= c < size


board = []
king_row = 0
king_col = 0
searched_queens = []

size = 8
for row in range(size):
    board.append(input().split())
    for col in range(size):
        if board[row][col] == "K":
            king_row, king_col = row, col

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_left': (-1, -1),
    'up_right': (-1, 1),
    'down_left': (1, -1),
    'down_right': (1, 1)
}

current_row, current_col = king_row, king_col
for direction in directions:
    next_row = current_row + int(directions[direction][0])
    next_col = current_col + int(directions[direction][1])
    while is_valid_position(next_row, next_col, size):
        if board[next_row][next_col] == "Q":
            searched_queens.append([next_row, next_col])
            break
        next_row += int(directions[direction][0])
        next_col += int(directions[direction][1])

if not searched_queens:
    print("The king is safe!")
else:
    print(*searched_queens, sep='\n')
