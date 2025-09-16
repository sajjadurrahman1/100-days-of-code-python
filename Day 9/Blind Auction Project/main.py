# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
bids = {} # empty dictionary
# TO DO 1
def user_input (): # functions to take the user input
  name= input("Enter your name:\n")
  bid_amount= int (input("how much do you want to bid $\n"))
  bids[name]= bid_amount # stored bid amount in the empty dictionary
  #return name, bid_amount
#name, bid_amount = user_input()


bidding_finished= False
while not bidding_finished: # using while loop for continuing the bidding
    user_input()
    other_bidders=input("Are there any other bidders? Type yes or no\n").lower()
    if other_bidders== "no":
        bidding_finished= True
    else:
        print("\n" *50)


highest_bidder= 0
winner=""
for bidder in bids:
    bid_amount= bids[bidder]
    if bid_amount > highest_bidder:
        highest_bidder= bid_amount
        winner = bidder
print(f"the winner is {winner} with bidding amount of {highest_bidder}")
