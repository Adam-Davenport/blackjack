from player import Player, Ai_Player
from random import shuffle
import cards

class Game():
	def __init__(self, player, count):
		self.deck = cards.Deck()
		self.players = []
		self.table_scores = []
		players = ['James', 'Carlton', 'Maxwell', 'Houston', 'Bigsby']
		players = players[0:count]
		self.players.append(Player(player))
		for p in players:
			print(p)
			self.players.append(Ai_Player(p))
		shuffle(self.players)
	def player_list(self):
		player_list = []
		for p in self.players:
			player_list.append(p.name)
		return ', '.join(player_list)
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
		high_score = 0
		winners = []
		for s in scores:
			score = scores[s]
			if score < 22:
				if score == high_score:
					winners.append(s)
				elif score > high_score:
					winners = [s]
					high_score = score
		print('')
		if high_score == 0:
			print('Everyone lost.')
		elif len(winners) == 1:
			print(winners[0] + ' is the winner, with {} points!'.format(high_score))
		else:
			print(', '.join(winners) + ' tied this round with {} points'.format(high_score))
	def play_game(self):
		print('The game is begining with {} players.'.format(len(self.players)))
		print('Current players: ' + self.player_list())
		print('Press enter to start the game.')
		input()
		print('Dealing 2 cards to each player.')
		self.deal()
		for p in self.players:
			self.play_round(p)
		self.find_winner()
	def play_round(self, p):
		self.table_scores = []
		print('\n' + p.name + '\n======================')
		inp = ''
		if p.calculate_score() == 21:
			print('Blackjack!')
			self.table_scores.append(21)
		else:
			while inp != 'd' and inp != 'p':
				p.view_hand()
				inp = p.play(self)
				if inp == 'd':
					self.draw(p)
					inp = ''
				if p.calculate_score() > 21:
					inp = 'p'
					print('{} is over 21 points and is out of the game.'.format(p.name))
				elif p.calculate_score() == 21:
					print('Blackjack! {} has 21 points!'.format(p.name))
					inp = 'p'
			self.table_scores.append(p.table_score())
