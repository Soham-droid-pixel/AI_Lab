import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("-----------")

def check_winner(b):
    win_states = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for combo in win_states:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return b[combo[0]]
    if ' ' not in b:
        return 'Tie'
    return None

def minimax(curr_board, is_maximizing):
    res = check_winner(curr_board)
    if res == 'X': return 1   # Utility for MAX win
    if res == 'O': return -1  # Utility for MIN win
    if res == 'Tie': return 0 # Utility for Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if curr_board[i] == ' ':
                curr_board[i] = 'X'
                score = minimax(curr_board, False)
                curr_board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if curr_board[i] == ' ':
                curr_board[i] = 'O'
                score = minimax(curr_board, True)
                curr_board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Simple Game Loop
print("AI (X) vs You (O)")
while True:
    print_board()
    if check_winner(board): break
    
    # Human Turn
    human_move = int(input("Enter move (0-8): "))
    if board[human_move] != ' ': continue
    board[human_move] = 'O'
    
    if check_winner(board): break
    
    # AI Turn
    print("\nAI is thinking...")
    ai_move = best_move()
    board[ai_move] = 'X'

print_board()
print(f"Game Over! Result: {check_winner(board)}")