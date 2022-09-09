import random 


# first we need to create a deck of cards 

deck = [1,2,3,4,5,6,7,8,9,'A','J','Q','K']
def multideck():
    for i in range (2):
        deck.extend(deck)


playerhand=[]
dealerhand = []

multideck()

print(deck)


#  create a hand for the player and the dealer

# calculate the total of the hands

# use game logic to check for winner