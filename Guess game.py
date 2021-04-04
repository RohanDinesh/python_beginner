answer = "giraffe"
count = 0
guess = ""
count_limit=3

print("Welcome to guessing game\nGuess the word correctly within " +str(count)+ " tries using the below clues to win")

print("\nclue 1: it is an animal")
print("clue 2:it lives on land")
print("clue 3:it is tall")

out_of_guesses=False

while(guess!=answer and not(out_of_guesses)):
    guess=input("enter your guess: ")
    count+=1
    if count == count_limit:
        out_of_guesses = True

if(guess!=answer):
    print("\nyou ran out of guesses\nYOU LOSE")

else:
    print("YOU WIN")

