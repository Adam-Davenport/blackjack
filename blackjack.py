from player import Player, Ai_Player
import cards

class Game():
    def __init__(self, players):
        self.deck = cards.Deck()
        self.players = []
        for p in players:
            self.players.append(Player(p))
    def reset_round(self):
        self.deck = Deck()
        for p in self.players:
            p.discard()
    def draw(self, player):
        card = self.deck.draw()
        player.draw(card)
        print(player.name + ' drew {} of {}'.format(card.rank, card.suite))

    def deal(self):
        for i in range(2):
            for p in self.players:
                c = self.deck.draw()
                p.hand.append(c)
    def find_winner(self):
        scores = {}
        for p in self.players:
            scores[p.name] = p.calculate_score()
        print(scores)

    def play_game(self):
        print('The game is begining with {} players.'.format(len(self.players)))
        print('Current players:')
        print('Dealing 2 cards to each player.')
        self.deal()
        for p in self.players:
            inp = ''
            while inp != 'd' and inp != 'p':
                p.view_hand()
                inp = input().lower()
                if inp == 'd':
                    self.draw(p)
                    inp = ''
        self.find_winner()
