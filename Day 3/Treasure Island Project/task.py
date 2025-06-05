print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

side_choice = input("Which side do you want to go? Left or Right\n")
if side_choice == "Right":
    print("Wasted!!! Game Over")
elif side_choice == "Left":
    print("Ok Great. You need to choose one more option!!")

    option_choice = input("Do you want to swim or wait?\n")
    if option_choice == "swim":
        print("Wasted!!! Game Over")
    elif option_choice == "wait":
        print("Now you need to choose a color.")
        color = input("Please choose a color: blue, red, or yellow\n")

        if color == "blue":
            print("Wasted!!! Game Over")
        elif color == "red":
            print("Wasted!!! Game Over")
        elif color == "yellow":
            print("Congratulations!!!! You won the game.")
        else:
            print("You have chosen a wrong color.")




