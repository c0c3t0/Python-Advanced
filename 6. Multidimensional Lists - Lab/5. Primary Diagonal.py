size = int(input())

matrix = []
for row in range(size):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = 0
for row in range(size):
    for col in range(size):
        if row == col:
            primary_diagonal += matrix[row][col]
            
print(primary_diagonal)
