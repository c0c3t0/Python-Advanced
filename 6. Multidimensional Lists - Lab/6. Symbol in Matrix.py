num = int(input())

matrix = []
for row in range(num):
    matrix.append(list(input()))

found = False
result = ()
symbol = input()
for row in range(num):
    for col in range(num):
        if matrix[row][col] == symbol:
            result = row, col
            found = True
            break
    if found:
        break

print(result if found else f"{symbol} does not occur in the matrix")
