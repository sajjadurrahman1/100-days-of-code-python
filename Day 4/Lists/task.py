import random
friends= ["alice","bob", "charlie", "david", "emanuel"]
#1st option
print(random.choice(friends))
#2nd option
random_index =random.randint(0,4)
print(friends[random_index])