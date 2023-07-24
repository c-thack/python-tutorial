secret_word = "giraffe"
guess = ""
guess_count = 0
max_guess_count = 3

while guess != secret_word and guess_count < max_guess_count:
    guess = input("Enter a guess: ")
    guess_count +=1

if guess == secret_word:
    print("Success!")
else:
    print("No good :(")

