# put all the ttt exercises together and make a working game

# draws an empty, square board
def empty_draw_board(board_size):
    for i in range(board_size):
        print(" ---" * board_size + "\n" + "|   " * (board_size + 1))
    print(" ---" * board_size)


# draws and updated game board after plays have been made
def update_draw_board(board):
    board_size = len(board)
    for i in range(board_size):
        print("\n" + " ---" * board_size)
        print("|", end="")
        for j in range(board_size):
            print(f" {players[board[i][j]]} |", end="")
    print("\n" + " ---" * board_size)


# checks for a tic-tac-tow winner (3 in a row) and returns the winner if there is one
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0


# requests a tic-tac-tow play from the players in the form of row,col
def make_a_play(board, player):
    valid = False
    while not valid:
        # since we're sticking to tic-tac-tow here, could also just use the input string as a list
        play = input(f"Player {player}, make your pick (row,col): ").strip().split(",")
        play = [int(play[0]), int(play[1])]
        if board[play[0]][play[1]] != 0:
            print("Spot already taken.")
        else:
            valid = True
    board[play[0]][play[1]] = player


# dictionary for player tokens; 0 is empty space, player 1 is X, player 2 is O
players = {0: " ", 1: "X", 2: "O"}
# initiate empty board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
play_count = 0
winner = 0

print("Let's play tic-tac-toe!")
empty_draw_board(3)

make_a_play(board, 1)
play_count += 1
update_draw_board(board)

while play_count < 5:
    make_a_play(board, 2)
    play_count += 1
    update_draw_board(board)

    make_a_play(board, 1)
    play_count += 1
    update_draw_board(board)

winner = check_win(board)
while play_count < 9 and winner == 0:
    make_a_play(board, 2)
    play_count += 1
    update_draw_board(board)
    winner = check_win(board)
    if winner > 0:
        print(f"Player {winner} wins!")
        break

    make_a_play(board, 1)
    play_count += 1
    update_draw_board(board)
    winner = check_win(board)
    if winner > 0:
        print(f"Player {winner} wins!")
        break

print("end")
