rows, cols = map(int, input().split())

matrix = []

for r in range(rows):
    matrix.append(list(input().split()))

command = input().split()
while not command[0] == "END":
    if not command[0] == "swap":
        print("Invalid input!")
    elif not len(command) == 5:
        print("Invalid input!")
    else:
        r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if 0 > r1 or r1 >= rows or 0 > r2 or r2 >= rows or 0 > c1 or c1 >= cols or 0 > c2 or c2 >= cols:
            print("Invalid input!")
        else:
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in range(rows):
                print(*matrix[row])
    command = input().split()
