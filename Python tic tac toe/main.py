def drawboard(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def boardfull(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

board = [[' ' for _ in range(3)] for _ in range(3)]
drawboard(board)


def drawboardindex(board):
    line = "-------------"
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            print(f"| {cell} ", end="")
        print("|")
        print(line)

drawboardindex(board)


