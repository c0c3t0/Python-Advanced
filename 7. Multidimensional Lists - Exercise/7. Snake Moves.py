rows, cols = map(int, input().split())
snake = list(input())

matrix = []
snake_index = 0

for r in range(rows):
    matrix.append([0 for el in range(cols)])

for r in range(rows):
    for c in range(cols):
        matrix[r][c] = snake[snake_index]
        snake_index += 1
        if len(snake) == snake_index:
            snake_index = 0

for row in range(rows):
    if row % 2 == 1:
        matrix[row].reverse()
    print(''.join([str(x) for x in matrix[row]]))
