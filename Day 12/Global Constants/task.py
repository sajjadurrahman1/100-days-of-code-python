import random
from art import logo

"""""using compare function to guess the correct number """

def compare(correct_number):
    """i will try to use a if block for guessing the perfect number but my plan is randomly choose a number between 1 to 100
       and then compare the number."""
    guess_the_num = int(input("enter the number\n"))
    if guess_the_num > correct_number:
        print("Too high\n")
    elif guess_the_num < correct_number:
        print("too low\n")
    else:
        print(f"you have done it\n  the correct number is {correct_number}")
        return True
    return False

def guess_num():
    correct_number = random.randint(1, 100)
    numb_of_attempt=0
    if difficulty_level== "hard":
        numb_of_attempt = 5
    elif difficulty_level== "easy":
        numb_of_attempt = 10
    else:
        print("CHUDLINGPONG input")
    remaining_attempt= numb_of_attempt
    for number in range(numb_of_attempt):

        print(f"You have {remaining_attempt} attempts remaining to guess the number.")
        remaining_attempt -= 1
        if compare(correct_number):
            break
    print(f"correct number {correct_number}")

"""the code starts from here"""

print(logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")
difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
guess_num()