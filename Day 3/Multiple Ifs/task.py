print("welcome to the rollercoaster")
height=int(input("what is your height in cm?"))
bill=0
if height >=120:
    print("you can ride the rollercoaster")
    age=int(input("how old are you?"))
    if age <= 12:
        bill=5
        print("child tickets are 5$")
    elif age <= 18:
        bill=7
        print("youth tickets are 7$")
    else:
        print("Adult tickets are §12")

    wants_photo = input("Do you want to take a photo? Type y for yes and n for no")
    if wants_photo == "y":
        # add §3 to their bill
       bill +=3
       print(f"your final bill is {bill}")
else:
    print("sorry you have to grow taller before you can ride")