import sys

rows, cols = map(int, input().split(", "))

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = - sys.maxsize
biggest_sum = 0
position = None

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        biggest_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if biggest_sum >= max_sum:
            max_sum = biggest_sum
            position = (row, col)

row, col = position
print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max_sum)
