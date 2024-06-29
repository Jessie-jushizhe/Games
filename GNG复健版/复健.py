import random

steps=0
random_number=random.randint(1,100)

print("Welcome to the guess number game! Please choose a number between 1 and 100.")

while steps<20:
    print("Guess the number between 1 and 100.")
    guess=int(input())
    steps += 1

    if guess>random_number:
        print("Your guess is too high.")

    if guess<random_number:
        print("Your guess is too low.")

    if guess==random_number:
        break

if guess==random_number:
    print("Congrats! You guessed the number in {} steps.".format(steps))

if guess!=random_number:
    print("I'm sorry but your guess is wrong.")