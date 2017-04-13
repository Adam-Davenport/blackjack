
class Player():
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.type = 'player'
    def discard(self):
        self.hand = []
        return cards
    def draw(self, card):
        self.hand.append(card)
    def calculate_score(self):
        score = 0
        for c in self.hand:
            value = c.value()
            if value != 11:
                score += value
            else:
                if score + 11 > 21:
                    score += 1
                else:
                    score += 11
        return score
    def view_hand(self):
        print('Current hand:')
        for c in self.hand:
            print('{} of {}'.format(c.rank, c.suite))

class Ai_Player(Player):
    def __init__(self):
        self.hand = []
        self.type = 'computer'
