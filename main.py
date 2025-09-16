import random
from art import logo2
print(logo2)
print("Welcome to the number guessing game ..!")
print("I am thinking of the number from 1 to 100..!")

# create a list of numbers from 1 to 100
number_list = list(range(1, 101))

# system randomly selects one number from the list
computer_guess = (random.choice(number_list))

# ask the user to choose difficulty level
user_choice = input("Choose the difficulty. Type 'easy' or 'hard'.")


# function to handle the guessing attempts
def attempt(count):
    # show how many attempts are left
    print(f"you have {count} attempts remaining to guess the number")

    # take the user’s guess (convert input to integer)
    guessed_num = int(input("Make a guess:"))

    # reduce the attempt count by 1 after each guess
    count -= 1

    # check if the guess is correct
    if guessed_num == computer_guess:
        print(f"you got it ! The answer was {computer_guess}")
        return  # end the function if guessed correctly

    # if guess is higher than the computer’s number
    elif guessed_num > computer_guess:
        print("Too High")

    # if guess is lower than the computer’s number
    elif guessed_num < computer_guess:
        print("Too Low")

    # if there are still attempts left, ask again
    if count != 0:
        print("Guess again")
        attempt(count)  # recursive call with reduced attempts

    # if no attempts left, player loses
    else:
        print(f"you ran out of attempts. YOU LOOSE....!\n The number was {computer_guess}")


# start the game depending on chosen difficulty
if user_choice == "easy":
    attempt(10)  # easy mode → 10 attempts
else:
    attempt(5)  # hard mode → 5 attempts



