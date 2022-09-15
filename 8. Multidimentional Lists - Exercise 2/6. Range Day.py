def is_valid_position(r, c):
    return 0 <= r < 5 and 0 <= c < 5


def get_next_position(direction, r, c, steps):
    if direction == "up":
        return r - steps, c
    elif direction == "down":
        return r + steps, c
    elif direction == "left":
        return r, c - steps
    return r, c + steps


matrix = []
start_row = 0
start_col = 0
all_targets = []

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            start_row, start_col = row, col
        if matrix[row][col] == "x":
            all_targets.append([row, col])

commands_count = int(input())
directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
shot_targets = []

for i in range(commands_count):
    if len(all_targets) == len(shot_targets):
        break
    cmd = input().split()
    command, direction = cmd[0], cmd[1]
    current_row, current_col = start_row, start_col
    if command == "move":
        steps = int(cmd[2])
        next_step_row, next_step_col = get_next_position(direction, current_row, current_col, steps)
        if not is_valid_position(next_step_row, next_step_col):
            continue
        if not matrix[next_step_row][next_step_col] == ".":
            continue
        start_row, start_col = next_step_row, next_step_col
    elif command == "shoot":
        for direct, step in directions.items():
            if direct == direction:
                shot_row, shot_col = current_row, current_col
                while is_valid_position(shot_row, shot_col):
                    next_shot_row, next_shot_col = step(shot_row, shot_col)
                    if not is_valid_position(next_shot_row, next_shot_col):
                        break
                    if matrix[next_shot_row][next_shot_col] == "x":
                        matrix[next_shot_row][next_shot_col] = "."
                        shot_targets.append([next_shot_row, next_shot_col])
                        break
                    shot_row, shot_col = next_shot_row, next_shot_col

if len(all_targets) == len(shot_targets):
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {len(all_targets) - len(shot_targets)} targets left.")
for target in shot_targets:
    print(target)
