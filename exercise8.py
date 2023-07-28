# Make a two-player Rock-Paper-Scissors game.

replay = True
plays = ["rock", "paper", "scissors"]

while replay:
    player1 = input("Player 1 - rock, paper, or scissors: ").lower()
    player2 = input("Player 2 - rock, paper, or scissors: ").lower()

    if player1 in plays and player2 in plays:
        if player1 == player2:
            print("Tie!")
        elif player1 == "rock":
            if player2 == "paper":
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        elif player1 == "paper":
            if player2 == "scissors":
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        elif player1 == "scissors":
            if player2 == "rock":
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
    else:
        print("Invalid input")

    response = input("Play again? y or n: ").lower()  # could add validation here too
    if response == "n":
        replay = False
