import cards

class Player():
    def __init__(self):
        self.hand = []
    def discard(self):
        self.hand = []
        return cards
    def draw(self, card):
        self.hand.append(card)

class Game():
    def __init__(self, players):
        self.deck = cards.Deck()
        self.players = []
        for p in range(players):
            self.players.append(Player())
    def calculate_score(self, hand):
        score = 0
        for c in hand:
            value = c.value
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
    def play_game(self):
        print('The game is begining with {} players.'.format(len(self.players)))
        print('Dealing 2 cards to each player.')
        self.deal()
        for p in self.players:
            inp = lower(input())
            while inp != 'y' or inp != 'n':
                print('Value of your current hand: {}. Would you like to draw or pass?'.format(self.calculate_score(p.hand)))
                inp = lower(input())
                if inp == 'y':
                    p.append(self.draw())
