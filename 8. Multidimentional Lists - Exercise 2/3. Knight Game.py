def in_board(board, row, col):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return False
    return board[row][col] == "K"


def count_knights_in_range(board, row, col):
    result = 0
    if in_board(board, row - 2, col - 1):
        result += 1
    if in_board(board, row - 2, col + 1):
        result += 1
    if in_board(board, row + 2, col - 1):
        result += 1
    if in_board(board, row + 2, col + 1):
        result += 1
    if in_board(board, row - 1, col - 2):
        result += 1
    if in_board(board, row - 1, col + 2):
        result += 1
    if in_board(board, row + 1, col - 2):
        result += 1
    if in_board(board, row + 1, col + 2):
        result += 1
    return result


size = int(input())

board = []
for _ in range(size):
    board.append(list(input()))

removed_knights = 0
while True:
    max_kills, knight_row, knight_col = 0, 0, 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == "K":
                kills = count_knights_in_range(board, row, col)
                if max_kills < kills:
                    max_kills, knight_row, knight_col = kills, row, col
    if max_kills == 0:
        break
    board[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)