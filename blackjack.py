import random
from secrets import choice 


# first we need to create a deck of cards 

deck = [2,3,4,5,6,7,8,9,'A','J','Q','K']
def multideck():
    for i in range (2):
        deck.extend(deck)


playerhand=[]
dealerhand = []

multideck()

print(deck)


#  create a hand for the player and the dealer

# deal cards
def deal(turn):
    drawnCard = random.choice(deck)
    turn.append(drawnCard)
    deck.remove(drawnCard)

# calculate the total of the hands
def handTotal(turn):
    total = 0
    for card in turn:
        if card in range (1,11):
            total += card

# use game logic to check for winner