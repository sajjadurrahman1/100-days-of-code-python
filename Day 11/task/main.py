import random
from art import logo
"""function for random card choice"""


def deal_card():
    """return a random card"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)



def compare(user_comparing_score, computer_comparing_score):
    if computer_comparing_score == user_comparing_score:
        return "It's a draw"
    elif computer_comparing_score == 0:
        return "You lost and the computer won the game"
    elif user_comparing_score > 21:
        return "You lost"
    elif computer_comparing_score > 21:
        return "You won"
    elif user_comparing_score > computer_comparing_score:
        return "You won"
    else:
        return "You lost"


def play_again():
    print(logo)
    user_card = []
    computer_card = []
    computer_score= 1
    user_score= 1
    is_game_over = False


    """using for loop to store two cards for user"""
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"the user cards are {user_card} and the user score is {user_score}")
        print(f"computer card {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_new_cards= input("Type 'y' to deal new cards and type 'n' to pass\n").lower()
            if draw_new_cards== "y":
                user_card.append(deal_card())
            else:
                is_game_over =True

    while computer_score < 17 and computer_score != 0:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        print(f"the computer score is {computer_score}")

    print(compare(user_score, computer_score))

while input("do you want to play blackjack  ? Type 'y' to play and 'n' to pass\n").lower() == "y":
    print("\n"*20)
    play_again()