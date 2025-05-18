print("welcome to the rollercoaster")
height=int(input("what is your height?"))
age=int(input("enter your age"))
if height >= 120:
    print("you r allowed to ride ")
    if age <12:
        print("pay 5$")12
    elif age <= 18:
       print("you need to pay 12$")
    else:
       print("you need to pay 18$")
else:
    print("you are not enough tall to have a ride")
