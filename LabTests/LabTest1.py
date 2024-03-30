import random

# Part 2
def get_guess():
    """Function that forces the user to input a three-digit number"""
    valid_digits = "0123456789"

    while True:
        guess = input("Guess a three digit number: ")

        if len(guess) != 3:
            print("Please enter a three digit number")
            continue


        for digit in guess:
            if digit not in valid_digits:
                print("Only digits from 0-9 are valid")
                break
        else:
            return guess


# Part 3
def get_hints(guess, secret_code):
    """ Function that returns the necessary tips based on the secred code and user guess"""
    output = ""

    for i, n in enumerate(guess):

        if n == secret_code[i]:
            output += "Bullseye "

        if n in secret_code and n != secret_code[i]:
            output += "Off-target "

        if n not in secret_code:
            output += "Null "

    return output


# Part 1
secret_code = [str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))]

N = 10  # Max number of guesses

print('''Welcome to 'Conundrum Code'. Try to guess the three number digit.\n\nHere are some clues:
When I say 'Off-target' that means one of your digits is correct but in the wrong position.
When I say 'Bullseye' that means one of your digits is correct but in the right position.
When I say 'Null' that means one of your digits is incorrect and in the wrong position.''')

current_guess = 0

# Part 4 and 5
while current_guess < N:
    guess = get_guess()

    output = get_hints(guess, secret_code)

    if output == "Bullseye Bullseye Bullseye ":
        print("You got it!")
        restart = input("Do you want to play again? (y/n)").lower()
        if restart == "n":
            print("Thank you for playing")
            break
        else:
            current_guess = 0
            secret_code = [str(random.randint(0, 9)), str(random.randint(0, 10)), str(random.randint(0, 9))]
            continue
    else:
        print(output)

    current_guess += 1

    if current_guess == N:
        print("You lost! The code was", secret_code)
        restart = input("Do you want to play again? (y/n)").lower()
        if restart == "n":
            print("Thank you for playing")
            break
        else:
            current_guess = 0
            secret_code = [str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))]