def is_valid_position(r, c, size):
    return 0 <= r < size and 0 <= c < size


def get_next_position(direction, r, c):
    if direction == "up":
        return r - 1, c
    elif direction == "down":
        return r + 1, c
    elif direction == "left":
        return r, c - 1
    return r, c + 1


def get_houses_in_range(size, r, c):
    houses = []
    if is_valid_position(r - 1, c, size):
        houses.append([r - 1, c])
    if is_valid_position(r + 1, c, size):
        houses.append([r + 1, c])
    if is_valid_position(r, c - 1, size):
        houses.append([r, c - 1])
    if is_valid_position(r, c + 1, size):
        houses.append([r, c + 1])
    return houses


presents = int(input())
size = int(input())

neighborhood = []
santa_row = 0
santa_col = 0
all_nice_kids = 0

for row in range(size):
    neighborhood.append(input().split())
    for col in range(size):
        if neighborhood[row][col] == "S":
            santa_row, santa_col = row, col
            neighborhood[row][col] = '-'
        if neighborhood[row][col] == "V":
            all_nice_kids += 1
nice_kids = all_nice_kids

while not presents == 0:
    command = input()
    if command == "Christmas morning":
        break
    next_row, next_col = get_next_position(command, santa_row, santa_col)
    if neighborhood[next_row][next_col] == "V":
        nice_kids -= 1
        presents -= 1

    elif neighborhood[next_row][next_col] == "C":
        houses_in_range = get_houses_in_range(size, next_row, next_col)
        for r, c in houses_in_range:
            if neighborhood[r][c] == "V":
                presents -= 1
                nice_kids -= 1
            if neighborhood[r][c] == "X":
                presents -= 1
            neighborhood[r][c] = '-'

    neighborhood[santa_row][santa_col] = '-'
    neighborhood[next_row][next_col] = 'S'
    santa_row, santa_col = next_row, next_col

if presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")
for row_elements in neighborhood:
    print(' '.join(row_elements))
if nice_kids == 0:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
