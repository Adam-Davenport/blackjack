from random import randint
from blackjack import Game

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
			if value < 11:
				score += value
			elif value < 14:
				score += 10
			else:
				if score + 11 > 21:
					score += 1
				else:
					score += 11
		return score
	def table_score(self):
		score = 0
		table = self.hand[1::]
		for c in table:
			value = c.value()
			if value < 11:
				score += value
			elif value < 14:
				score += 10
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
	def play(self):
		print('Would you like to draw (d) or pass (p)?')
		inp = input().lower()
		return inp

class Ai_Player(Player):
	def __init__(self, name):
		Player.__init__(self, name)
		self.hand = []
		self.type = 'computer'
	def play(self):
		if self.calculate_score() < 18:
			return 'p'
		else:
			return 'd'
