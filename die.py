# The die class

from random import randint

class Die():
	""" A class repensenting a single die """
	
	def __init__(self, num_sides=6):
		"""Assume its a six-sided die"""
		self.num_sides = num_sides
		
	def roll(self):
		""" Return a random number value between 1 and the number of sides. """
		return randint(1, self.num_sides)
