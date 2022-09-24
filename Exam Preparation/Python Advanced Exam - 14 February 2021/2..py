def is_valid_position(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    elif direction == 'down':
        return r + 1, c
    elif direction == 'left':
        return r, c - 1
    elif direction == 'right':
        return r, c + 1


size = int(input())

field = []
player_row = 0
player_col = 0

for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == "P":
            player_row, player_col = row, col

commands = {'up', 'down', 'right', 'left'}
path = []
coins = 0
lose = False

while True:
    command = input()
    if command not in commands:
        continue
    next_row, next_col = get_next_position(command, player_row, player_col)
    if not is_valid_position(size, next_row, next_col) or field[next_row][next_col] == "X":
        coins = coins // 2
        lose = True
        break
    else:
        path.append([next_row, next_col])
        coins += int(field[next_row][next_col])
        player_row, player_col = next_row, next_col
    if coins >= 100:
        break

if not lose:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*path, sep='\n')