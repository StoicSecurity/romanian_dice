# Classes to import
import random
import pygame as pg

import sys

from player import Player
from die import Die
from settings import Settings

# Main file for romainian dice
continueGame = True
current_player = Player()


def gatherPlayerInfo():
	print("\nFirst we need some information about you...")
	try:
		current_player.starting_cash = int(input("How much money do you have in your pocket?"))
		
		
	except ValueError:
		print("That can't be in your pocket")
		gatherPlayerInfo()
		
	current_player.namename = input("Now we just need to know your name: ")
	
	print("Welcome, " + current_player.name + "\nYou have $" + 
	str(current_player.starting_cash))
		

def checkUserInput():
	userAnswer = input("\n" + current_player.name.title() + 
	" Do you know the rules? (y/n)")

	if userAnswer.lower() == 'y' or userAnswer.lower() == 'yes':
		startGame()
	
	elif userAnswer.lower() == 'n'  or userAnswer.lower() == 'no':
		print("Lets go over the rules!")
		showGameRules() 

	else:
		print('that is not a "y" or a "n"!')
		checkUserInput()

def showGameRules():
	print("1.) Choose a bet")
	print("2.) Make a selection of the betting result.")
	print("3.) hope for the best!")
	startGame()

def startGame():
	#maybe play that push it to the limit song at the start
	
	print("\nLet's start the game!")
	
	
	
	
def takeBet():
	# global bet
	
	try: 
		print("\nCurrent money in your pocket $" + str(current_player.starting_cash))
	
		current_player.bet = int(input("\nHow much would you like to bet?"))
		
		
		if current_player.bet <= 0:
			print("\nYou can't bet less than zero!")
			takeBet()
	
		elif current_player.bet > current_player.starting_cash:
			print("\nYou can't bet more than what you have!")
			takeBet()
		
		elif current_player.bet > 0 and int(current_player.bet) <= current_player.starting_cash:
			print("You have bet $" +  str(current_player.bet))
			current_player.starting_cash -= current_player.bet
			print("\nRemaining money $" + str(current_player.starting_cash))
		
		else: 
			print("\nNot sure what you wanted")
			takeBet()
	
	except ValueError:
		print("You can't bet that!")
		takeBet()

def checkUserBets():
	""" gives a selection of bets to make"""
	global pocketMoney
	global bet
	
	betsToMake = "\nSelect an Option, enter a number"
	betsToMake += "\n1.) Odds"
	betsToMake += "\n2.) Evans"
	
	print(betsToMake)
	try:
		selection = int(input())
		userBet(selection)
		
	
	except ValueError:
		print("Please select an option from above")
		checkUserBets()

def userBet(selection):
	global bet
	global pocketMoney
	
	result = die_1.roll()
	print("\nThe die rolled is: " + str(result))
	
	if selection == 1:
		if result % 2 != 0:
			print("You won!")
			winnings = (current_player.bet*1.5)
			current_player.starting_cash += winnings 
			
		else:
			print("Sorry you lose your bet")
			
			
	elif selection == 2:
		if result % 2 == 0:
			print("You won!")
			winnings = (current_player.bet*1.5)
			current_player.starting_cash += winnings 
			
		else:
			print("Sorry you lose your bet")		
			
###############################################################################
# Start of the game 
###############################################################################
rd_settings = Settings()

startUpMessage = "Welcome to romanian dice game!"
startUpMessage += "\nThe safe and fun romanian dice game simulator"

print(startUpMessage)

pg.init()
pg.font.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((rd_settings.scrWidth, rd_settings.scrHeight))
pg.display.set_caption("Romanian Dice Simulator")

image = pg.image.load('images/putin_8bit_final.png').convert()


myfont = pg.font.SysFont('Comic Sans MS', 64)

textsurface = myfont.render('TEST TEXT', False, (0, 0, 0))
#gatherPlayerInfo()
#checkUserInput()

die_1 = Die()



while continueGame:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
	screen.fill(rd_settings.bg_color)
	screen.blit(image, (700,300))
	screen.blit(textsurface,(0,0))
	
	#takeBet()
	#checkUserBets()
	
	#if current_player.starting_cash <= 0:
	#	continueGame = False
		
	#if continueGame == False:
	#	print("\n Looks like you lost all your money! Sucks!")
	
	pg.display.flip()
	clock.tick(rd_settings.FPS)
