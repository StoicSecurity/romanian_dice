# Button class.

import pygame as pg

class Buttons():
	
	def __init__(self, rd_settings, screen, msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Standard button properties
		self.width, self.height = 200, 50
		self.button_color = (0, 225, 0)
		self.button_color_hover = (0, 255, 0)
		self.text_color = (255,255,255)
		self.my_font = pg.font.Font('images/8bit.ttf', 128)
		
		#Build the buttons rect object and center it
		self.rect = pg.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		# The button message needs to be prepped only once. 
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		""" Turn msg into a rendered image and center text on the button. """
		self.msg_image = self.my_font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		# Draw a blank button  the draw the message
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)	
		
		
