"""if you create a variable inside the function then it needs to be called inside the function
it is a local variable. But if you use any if else condition and declare the variable inside the if or else part
and called it outside the function it will print. it can be if block ,
while loop or for loop or anything that has separate indentation
that variable will not called as local variable"""

game_level = 3
enemies=["zombie", "Anaconda", "Alien"]
def create_enemy():
    generated_enemy=""
    if game_level < 5:
        generated_enemy=enemies[0]
    print(generated_enemy)
create_enemy()



