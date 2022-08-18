rows, cols = map(int, input().split())

matrix = []

for row in range(rows):
    matrix.append(input().split())

counter = 0

for col in range(cols - 1, 0, -1):
    for row in range(rows - 1, 0, -1):
        if matrix[row][col] == matrix[row - 1][col] and matrix[row][col] == matrix[row][col - 1] \
                and matrix[row][col] == matrix[row - 1][col - 1]:
            counter += 1
print(counter)