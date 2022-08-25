def check_is_coordinates_valid(rows, r, c):
    if 0 <= r < rows and 0 <= c < rows:
        return True


rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

command = input()
while not command == "END":
    cmd, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if check_is_coordinates_valid(rows, row, col):
        if cmd == "Add":
            matrix[row][col] += value
        elif cmd == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

for row in matrix:
    print(' '.join([str(x) for x in row]))
