rows = int(input())

matrix = []
for row in range(rows):
    matrix.extend([int(el) for el in input().split(", ")])

print(matrix)
