import random

# User must give number between two certain values until correct.

def person_guess(x, y):
    answer = random.randint(x, y)
    guess = 0.1

    while guess != answer:
        guess = int(input(f"Enter a number between {x} and {y}: "))
        if guess > answer:
            print("Too high, guess again!")
        elif guess < answer:
            print("Too low, guess again!")

    print(f"You guessed correctly! The secret number is {answer}.")


def computer_guess(answer):
    """Computer must guess number b/w 1 and 10."""

    guess_count = 0
    computer_guess = random.randint(1, 10)

    while guess_count < 3:
        guess_count += 1
        if computer_guess < answer:
            print(f"Guess {guess_count}: {computer_guess} --> too low")
            computer_guess = random.randint(computer_guess + 1, 10)
        elif computer_guess > answer:
            print(f"Guess {guess_count}: {computer_guess} --> too high")
            computer_guess = random.randint(1, computer_guess - 1)
        else:
            print(f"Guess {guess_count}: {computer_guess} --> correct! \n"
                  f"Was able to guess on attempt {guess_count}.")
            break

    if computer_guess != answer:
        print(f"Could not guess.")

computer_guess(5)







