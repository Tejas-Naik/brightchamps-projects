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

def movement():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    while True:
        drawboard(board)
        player = players[current_player]
        
        print(f"Player {player}'s turn.")
        row, col = movement()

        if board[row][col] == ' ':
            board[row][col] = player

            if winner(board, player):
                drawboard(board)
                print(f"Player {player} wins!")
          
                play()
                break
            elif boardfull(board):
                drawboard(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player
        else:
          print("That cell is already fille please Try again.")

play()

