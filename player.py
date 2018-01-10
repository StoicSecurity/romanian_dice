# A custom player class for romanian dice game

class Player():
	""" A class repensenting a player """
	
	def __init__(self):
		"""A player class for holding basic player information"""
		self.name = ""
		self.starting_cash = 0
		self.bet = 0
		
	def setName(self, name):
		"""sets the player name"""
		self.name = name
	
	def setStartingCash(self, cash):
		"""sets the player starting cash"""
		self.starting_cash = cash
		
	def setBet(self, bet):
		"""sets the players bet"""
		self.bet = bet
