rows, cols = map(int, input().split(", "))

matrix = []
row_sum = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    row_sum += sum(matrix[row])

print(row_sum)
print(matrix)