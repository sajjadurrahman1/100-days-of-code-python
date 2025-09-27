  #  enemies = 1


  #  def increase_enemies():
      #  enemies = 2
#       print(f"enemies inside function: {enemies}")


    #increase_enemies()
#    print(f"enemies outside function: {enemies}")


# global scope= when a variable is declared  at the top of the function.Means it is at the top of the declared function
# local scope = when the variable is declared inside the function.

player_health= 10 # global variable
def game():
    def drink_energy():
        potion_strength=2 # local variable
        print(player_health)
    drink_energy()
#print(player_health)
game()