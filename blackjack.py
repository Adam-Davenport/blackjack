import cards

class Player():
    __init__(self):
        self.hand = []
    def discard(self):
        self.hand = []
        return cards
    def draw(self, card):
        self.hand.append(card)

class Game():
    __init__(self, players):
        self.deck = Deck()
        self.players = []
        for p in players:
            players.append(Player())
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
    def play_game(self):
        print('The game is begining with ')
    def reset_round(self):
        self.deck = Deck()
        for p in self.players:
            p.discard()
