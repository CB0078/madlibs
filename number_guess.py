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


def computer_guess(lower_bound, upper_bound, guess_limit):
    """Computer must guess number b/w 1 and 10."""

    guess_count = 0

    while guess_count < guess_limit:
        computer_guess = random.randint(lower_bound, upper_bound)
        guess_count += 1
        feedback = input(f"Is {computer_guess} too high (H), too low (L), or correct (C)?: ").lower()
        if feedback == 'l':
            print(f"Guess {guess_count}: {computer_guess} --> too low")
            lower_bound = computer_guess + 1
            computer_guess = random.randint(lower_bound, upper_bound)
        elif feedback == 'h':
            print(f"Guess {guess_count}: {computer_guess} --> too high")
            upper_bound = computer_guess - 1
            computer_guess = random.randint(lower_bound, upper_bound)
        elif feedback == 'c':
            print(f"Guess {guess_count}: {computer_guess} --> correct! \n"
                  f"Was able to guess on attempt {guess_count}.")
            break

    if feedback != 'c':
        print(f"Could not guess.")

computer_guess(1, 10, 3)







