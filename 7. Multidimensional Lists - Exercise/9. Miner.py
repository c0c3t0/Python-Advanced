from collections import deque

size = int(input())
moves = deque(input().split())

matrix = []
total_coals = 0
collected_coals = 0
player_position = []
for r in range(size):
    matrix.append(input().split())
    if 'c' in matrix[r]:
        total_coals += matrix[r].count('c')
    if 's' in matrix[r]:
        player_position = [r, matrix[r].index('s')]

end = False
while moves:
    current_move = moves.popleft()
    if collected_coals == total_coals:
        break
    if current_move == 'up':
        player_position = [player_position[0] - 1, player_position[1]]
        if player_position[0] not in range(len(matrix)) or player_position[1] not in range(0, size):
            player_position = [player_position[0] + 1, player_position[1]]
        else:
            if matrix[player_position[0]][player_position[1]] == "c":
                collected_coals += 1
                matrix[player_position[0]][player_position[1]] = "*"
            elif matrix[player_position[0]][player_position[1]] == "e":
                end = True
                break
    elif current_move == 'down':
        player_position = [player_position[0] + 1, player_position[1]]
        if player_position[0] not in range(len(matrix)) or player_position[1] not in range(0, size):
            player_position = [player_position[0] - 1, player_position[1]]
        else:
            if matrix[player_position[0]][player_position[1]] == "c":
                collected_coals += 1
                matrix[player_position[0]][player_position[1]] = "*"
            elif matrix[player_position[0]][player_position[1]] == "e":
                end = True
                break
    elif current_move == 'left':
        player_position = [player_position[0], player_position[1] - 1]
        if player_position[0] not in range(len(matrix)) or player_position[1] not in range(0, size):
            player_position = [player_position[0], player_position[1] + 1]
        else:
            if matrix[player_position[0]][player_position[1]] == "c":
                collected_coals += 1
                matrix[player_position[0]][player_position[1]] = "*"
            elif matrix[player_position[0]][player_position[1]] == "e":
                end = True
                break
    elif current_move == 'right':
        player_position = [player_position[0], player_position[1] + 1]
        if player_position[0] not in range(len(matrix)) or player_position[1] not in range(0, size):
            player_position = [player_position[0], player_position[1] - 1]
        else:
            if matrix[player_position[0]][player_position[1]] == "c":
                collected_coals += 1
                matrix[player_position[0]][player_position[1]] = "*"
            elif matrix[player_position[0]][player_position[1]] == "e":
                end = True
                break

if end:
    print(f"Game over! ({player_position[0]}, {player_position[1]})")
elif collected_coals == total_coals:
    print(f"You collected all coal! ({player_position[0]}, {player_position[1]})")
elif not moves:
    print(f"{total_coals-collected_coals} pieces of coal left. ({player_position[0]}, {player_position[1]})")
