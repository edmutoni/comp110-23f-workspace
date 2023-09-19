"""Game that only completes when you guess the right number"""

from random import randint
secret_num: int = randint(1,10)

guess: int = int(input("Guess a number between 1-10: "))
tries_count: int = 0
number_of_tries: int = 3
while guess != secret_num and tries_count < number_of_tries:
    print("Wrong")
    if (guess < 1) or (guess > 10):
        print("That's not between 1-10!")
    if guess > secret_num:
        print("Your guess was too high")
    else:
        print("Your guess was too low")
    guess = int(input("Guess again: "))
    tries_count = tries_count + 1
if guess == secret_num:
    print("You got it!")