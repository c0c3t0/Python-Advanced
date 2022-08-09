rows = int(input())

matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ") if int(el) % 2 == 0])

print(matrix)
