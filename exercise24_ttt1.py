# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print
# statement.


def draw_board(board_size):
    for i in range(board_size):
        print(" ---" * board_size + "\n" + "|   " * (board_size + 1))
    print(" ---" * board_size)


size = int(input("Enter size of square game board: "))
draw_board(size)
