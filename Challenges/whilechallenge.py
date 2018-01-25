import random

highest = 10
guess = 1
answer = random.randint(1, highest)

while guess != 0:
    guess = int(
        input("Please guess a number between 1 and {}: ".format(highest)))

    if guess == 0:
        print("You quit!")
        break
    elif guess < answer:
        print("Guess too low! Try again.")
    elif guess > answer:
        print("Guess too high! Try again.")
    else:
        print("You guessed correctly!")
        break
