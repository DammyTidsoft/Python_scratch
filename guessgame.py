#Guessing Game without limit
#secret_word ="Giraffe"
#guess=""
#while guess != secret_word:
#    guess = input("Guess the secret word ")
#print("You Win!")

#Setting a limit
secret_word ="Giraffe"
guess=""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the secret word ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You lost the Game")
else:
    print("You Win!")