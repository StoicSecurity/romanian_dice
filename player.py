# A custom player class for romanian dice game

class Player():
	""" A class repensenting a player """
	
	def __init__(self, name='', starting_cash=100):
		"""A player class for holding basic player information"""
		self.name = name
		self.starting_cash = starting_cash
