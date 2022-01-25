import random

# User must give number between two certain values until correct.

def number_guess(x, y):
    answer = random.randint(x, y)
    guess = 0.1

    while guess != answer:
        guess = int(input(f"Enter a number between {x} and {y}: "))
        if guess > answer:
            print("Too high, guess again!")
        elif guess < answer:
            print("Too low, guess again!")

    print(f"You guessed correctly! The secret number is {answer}.")

number_guess(0, 10)