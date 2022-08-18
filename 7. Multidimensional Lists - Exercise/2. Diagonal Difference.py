rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

primary = []
secondary = []
for row in range(rows):
    for col in range(rows):
        if row == col:
            primary.append(matrix[col][row])

c = rows - 1
for r in range(rows):
    if c >= 0:
        secondary.append(matrix[r][c])
        c -= 1
    else:
        break

print(f"{abs(sum(primary) - sum(secondary))}")
