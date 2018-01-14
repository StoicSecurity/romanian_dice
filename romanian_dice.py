# Classes to import
import random
import pygame as pg

import sys

from player import Player
from die import Die
from settings import Settings

import rd_game_functions as gf

# Main file for romainian dice
continueGame = True
current_player = Player()
rd_settings = Settings()		
			
###############################################################################
# Start of the game 
###############################################################################

pg.init()
pg.font.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((rd_settings.scrWidth, rd_settings.scrHeight))
pg.display.set_caption("Romanian Dice Simulator")

putin = pg.image.load('images/putin_8bit_final.png')

blankDie = pg.image.load('images/blankDie.png').convert()
eightBit = pg.font.Font('images/8bit.ttf', 128)


die_1 = Die()

###############################################################################
# Main Game Loop
###############################################################################

while continueGame:
	
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
	
	
	
	screen.fill(rd_settings.bg_color)
	gf.introPutin(screen, putin, blankDie, eightBit)

	
	pg.display.flip()
	
	clock.tick(rd_settings.FPS)
