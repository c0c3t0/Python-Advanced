from collections import deque


def is_valid_position(rows, cols, r, c):
    return 0 <= r < rows and 0 <= c < cols


def next_player_position(direction, row, col):
    if direction == "U":
        return row - 1, col
    elif direction == "D":
        return row + 1, col
    elif direction == "L":
        return row, col - 1
    elif direction == "R":
        return row, col + 1


def spread_bunnies(bunnies, row, col):
    all_bunnies = set()
    for r, c in bunnies:
        if is_valid_position(rows, cols, r - 1, c):
            all_bunnies.add((r - 1, c))
        if is_valid_position(rows, cols, r + 1, c):
            all_bunnies.add((r + 1, c))
        if is_valid_position(rows, cols, r, c - 1):
            all_bunnies.add((r, c - 1))
        if is_valid_position(rows, cols, r, c + 1):
            all_bunnies.add((r, c + 1))
    return all_bunnies


rows, cols = map(int, input().split())

matrix = []
bunnies = set()
player_row = 0
player_col = 0
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "P":
            player_row, player_col = (row, col)
            matrix[row][col] = "."
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = [el for el in input()]

won = None

for command in commands:
    move = command
    player_position_row, player_position_col = next_player_position(move, player_row, player_col)
    if not is_valid_position(rows, cols, player_position_row, player_position_col):
        won = True
    elif matrix[player_position_row][player_position_col] == "B":
        won = False
    if not won:
        player_row, player_col = player_position_row, player_position_col

    all_bunnies = spread_bunnies(bunnies, rows, cols)
    for r, c in all_bunnies:
        if r == player_position_row and c == player_position_col and not won:
            won = False
        matrix[r][c] = 'B'
    bunnies = set.union(all_bunnies, bunnies)

    if won is not None:
        break

for row_elements in matrix:
    print(''.join(row_elements))
if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
