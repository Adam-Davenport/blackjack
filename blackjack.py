import cards

class Player():
    def __init__(self, name):
        self.hand = []
        self.name = name
    def discard(self):
        self.hand = []
        return cards
    def draw(self, card):
        self.hand.append(card)

class Game():
    def __init__(self, players):
        self.deck = cards.Deck()
        self.players = []
        for p in players:
            self.players.append(Player(p))
    def calculate_score(self, hand):
        score = 0
        for c in hand:
            value = c.value()
            if value != 11:
                score += value
            else:
                if score + 11 > 21:
                    score += 1
                else:
                    score += 11
        return score
    def reset_round(self):
        self.deck = Deck()
        for p in self.players:
            p.discard()
    def draw(self):
        return self.deck.draw()
    def deal(self):
        for i in range(2):
            for p in self.players:
                c = self.draw()
                p.hand.append(c)
    def find_winner(self):
        for p in self.players:

    def play_game(self):
        print('The game is begining with {} players.'.format(len(self.players)))
        print('Current players:')
        print('Dealing 2 cards to each player.')
        self.deal()
        for p in self.players:
            inp = ''
            while inp != 'd' or inp != 'p':
                print('Value of your current hand: {}. Would you like to draw (d) or pass (p)?'.format(self.calculate_score(p.hand)))
                inp = input().lower()
                if inp == 'y':
                    p.draw(self.draw())
