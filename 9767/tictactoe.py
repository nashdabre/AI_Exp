import math

X, O, EMPTY = 'X', 'O', ' '

def game_over(b):
    lines = b + list(zip(*b)) + [[b[i][i] for i in range(3)], [b[i][2 - i] for i in range(3)]]
    return any(all(cell == lines[0][0] and cell != EMPTY for cell in line) for line in lines) or all(cell != EMPTY for row in b for cell in row)

def evaluate(b):
    if any(all(cell == X for cell in row) for row in b):
        return 1
    elif any(all(cell == O for cell in row) for row in b):
        return -1
    elif any(all(cell == X for cell in col) for col in zip(*b)):
        return 1
    elif any(all(cell == O for cell in col) for col in zip(*b)):
        return -1
    elif all(b[i][i] == X for i in range(3)) or all(b[i][2 - i] == X for i in range(3)):
        return 1
    elif all(b[i][i] == O for i in range(3)) or all(b[i][2 - i] == O for i in range(3)):
        return -1
    else:
        return 0

def minimax(b, d, m):
    if game_over(b) or d == 0:
        return evaluate(b)
    return max(minimax([row[:] for row in b], d - 1, not m) for row in b for cell in row if cell == EMPTY) if m else min(minimax([row[:] for row in b], d - 1, not m) for row in b for cell in row if cell == EMPTY)

def print_board(b):
    for row in b:
        print(' | '.join(row))
        print('-' * 5)

def play():
    b = [[EMPTY] * 3 for _ in range(3)]
    while not game_over(b):
        if EMPTY in [cell for row in b for cell in row]:
            human_move = tuple(map(int, input("Enter your move (row, column): ").split(',')))
            if b[human_move[0]][human_move[1]] == EMPTY:
                b[human_move[0]][human_move[1]] = O
            else:
                print("Invalid move! Try again.")
                continue
            print_board(b)
            if not game_over(b):
                ai_move = max([(r, c) for r in range(3) for c in range(3) if b[r][c] == EMPTY], key=lambda x: minimax([row[:] for row in b] if (x[0], x[1]) == x else copy.deepcopy(b), 5, True))
                b[ai_move[0]][ai_move[1]] = X
                print("AI's move:")
                print_board(b)
        else:
            break

    winner = 'AI' if any(all(cell == X for cell in row) for row in b) else 'You' if any(all(cell == O for cell in row) for row in b) else 'Nobody'
    print(f"The winner is: {winner}")

play()