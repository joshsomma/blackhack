import random
from card import Card

class Deck(object):
    def __init__(self):
        self.deck = []

        # set up deck vars
        self.suits = ('D','C','H','S')
        self.ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

        for s in self.suits:
            for r in self.ranks:
                self.deck.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()