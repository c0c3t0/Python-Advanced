size = int(input())

matrix = []

for i in range(size):
    matrix.append([int(el) for el in input().split()])

coordinates = input().split()
for cor in range(len(coordinates)):
    row, col = int(coordinates[cor][0]), int(coordinates[cor][2])
    bomb = matrix[row][col]
    if bomb > 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r in range(len(matrix)) and c in range(len(matrix[r])) and matrix[r][c] > 0:
                    matrix[r][c] -= bomb

alive_cells = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in range(size):
    print(*matrix[row])
