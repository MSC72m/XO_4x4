player1 = 'X'
player2 = 'O'
curr_player = player1
game_over = False
board = ["_" for _ in range(9)]  # Board should have 9 spaces for a 3x3 grid


def switch(curr_player):
    return player2 if curr_player == player1 else player1


def get_move(curr_player):
    move = input(f"Plz enter your move Player {curr_player}: ")
    return move


def print_board(board):
    for i in range(3):
        print(' | '.join(board[i*3:(i+1)*3]))


def validate_move(move):
    if 0 <= move < 9 and board[move] == "_":
        return True
    else:
        print("invalid move")
        return False
while not game_over:
    move = int(get_move(curr_player))
    if validate_move(move):
        print(f"Player {curr_player} moved to {move}")
        board[move] = curr_player
        curr_player = switch(curr_player)
        print_board(board)
