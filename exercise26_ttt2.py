# given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me
# which player won, if any.  The "board" will be a list of lists where 0 is empty, 1 is player 1's token, 2 is player
# 2's token.

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


# test cases
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(check_win(winner_is_2))
print(check_win(winner_is_1))
print(check_win(winner_is_also_1))
print(check_win(no_winner))
print(check_win(also_no_winner))