def is_inside(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_numbers(r, c):
    left = int(matrix[r][0])
    right = int(matrix[r][-1])
    up = int(matrix[0][c])
    down = int(matrix[-1][c])
    return left + right + up + down


size = 7

first_player, second_player = input().split(", ")
matrix = []

for r in range(size):
    matrix.append(input().split())

first_player_turn = True
first_player_score = 501
second_player_score = 501
throws_first = 0
throws_second = 0
first_player_won = False
second_player_won = False

while not first_player_won or not second_player_won:
    coordinates = input()[1:-1].split(", ")
    row, col = int(coordinates[0]), int(coordinates[1])

    if first_player_turn:
        first_player_turn = False
        throws_first += 1
        if not is_inside(size, row, col):
            continue
        if matrix[row][col].isdigit():
            first_player_score -= int(matrix[row][col])
        elif matrix[row][col] == "D":
            total_sum = get_numbers(row, col)
            first_player_score -= total_sum * 2
        elif matrix[row][col] == "T":
            sum = get_numbers(row, col)
            first_player_score -= sum * 3
        elif matrix[row][col] == "B":
            first_player_won = True
            break
        if first_player_score <= 0:
            first_player_won = True
            break
    else:
        first_player_turn = True
        throws_second += 1
        if not is_inside(size, row, col):
            continue
        if matrix[row][col].isdigit():
            second_player_score -= int(matrix[row][col])
        elif matrix[row][col] == "D":
            total_sum = get_numbers(row, col)
            second_player_score -= total_sum * 2
        elif matrix[row][col] == "T":
            sum = get_numbers(row, col)
            second_player_score -= sum * 3
        elif matrix[row][col] == "B":
            second_player_won = True
            break
        if second_player_score <= 0:
            second_player_won = True
            break

if first_player_won:
    print(f"{first_player} won the game with {throws_first} throws!")
else:
    print(f"{second_player} won the game with {throws_second} throws!")
