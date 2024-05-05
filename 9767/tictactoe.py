import random

def print_board(board):
    [print("|".join(row),"\n-----") for row in board]

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def player_move(board, player, move):
    row, col = move
    if board[row][col] != " ": return False
    board[row][col] = player
    return True

def minimax(board, depth, is_maximizing):
    scores = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = 'O' if is_maximizing else 'X'
                score = minimax(board, depth + 1, not is_maximizing)
                scores.append(score)
                board[row][col] = " "
    return max(scores) if is_maximizing else min(scores) if scores else 0

def ai_move(board, player):
    return random.choice([(row, col) for row in range(3) for col in range(3) if board[row][col] == " "])

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]

        if player == 'X':
            move = input("Enter your move as 'row,col' (e.g., 1,2): ")
            move = tuple(map(int, move.split(',')))
            while not (0 <= move[0] <= 2 and 0 <= move[1] <= 2) or not player_move(board, player, move):
                move = input("Invalid move. Try again: ")
                move = tuple(map(int, move.split(',')))
        else:
            move = ai_move(board, player)
            print(f"AI chooses {move[0]},{move[1]}")
            player_move(board, player, move)

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    main()
