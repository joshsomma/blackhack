class Hand(object):

    def __init__(self):
        self.cards = []
        self.points = 0
        card_vals = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

    def print_hand(self):
        for c in self.cards:
            print(c)

    def sum_points(self):
        for c in self.cards:
            self.points += card_vals[c.rank]