from random import shuffle

class Card():
    ranks = '1 2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')
    suites = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def index(self):
        return Card.ranks.index(self.rank)
    def value(self):
        return Card.ranks.index(self.rank)+1

class Deck():
    def __init__(self):
        self.cards = []
        for r in Card.ranks:
            for s in Card.suites:
                card = Card(r, s)
                self.cards.append(card)
    def shuffle(self):
        shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
