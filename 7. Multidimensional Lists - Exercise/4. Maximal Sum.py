import sys

rows, cols = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -sys.maxsize
position = None
for col in range(cols-2):
    for row in range(rows - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                      + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                      + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(f"Sum = {max_sum}")
print(matrix[row][col], matrix[row][col + 1], matrix[row][col + 2])
print(matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2])
print(matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2])
