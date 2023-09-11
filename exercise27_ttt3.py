# player input to tic tac toe board

def make_a_play(board, player):
    valid = False
    while not valid:
        play = input("Player %i, make your pick (row,col): " % player).strip().split(",")
        play = [int(play[0]), int(play[1])]
        if board[play[0]][play[1]] != 0:
            print("Spot already taken.")
        else:
            valid = True
    board[play[0]][play[1]] = players[player]


players = {1: "X", 2: "O"}

game = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
play_count = 0

make_a_play(game, 1)
play_count += 1
print(game)

while play_count < 9:
    make_a_play(game, 2)
    play_count += 1
    print(game)

    make_a_play(game, 1)
    play_count += 1
    print(game)

print("end")
