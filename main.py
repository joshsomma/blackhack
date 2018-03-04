from card import Card
from deck import Deck
from hand import Hand

##########################
# set up vars for the game
##########################
# holds values of cards
card_vals = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
# player starting chips
chips = 100
##########################
# /set up vars for the game
##########################

# --------------------- #

##########################
# helper functions
##########################

# ask player for a bet amount
def make_bet():
    while True:
        try:
            print('Enter your bet amount for this hand... ')
            bet_amount = int(input())
        except ValueError:
            print('Please enter an integer...')
            continue
        else:
            break

def hit():
    pass

def stand():
    pass

def game_step():
    pass

##########################
# /helper functions
##########################


# welcome message
print('Welcome to blackjack!')

# instantiate objects
game_deck = Deck()
game_deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()

player_hand.cards.append(game_deck.dealCard())
player_hand.cards.append(game_deck.dealCard())
print(player_hand)



# make_bet()
