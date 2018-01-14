import pygame as pg
import sys
from time import sleep

# a collection of game functions that is stored in the file

def bootUpScreen():
	"""Does stuff"""
	x=3

def introPutin(screen, putin, blankDie, eightBit):
	
	mouseX, mouseY = pg.mouse.get_pos()
	
	blankDie2 = blankDie
	titleText = eightBit.render('Romanian Dice Simulator', False, (0, 0, 0))
	startText = eightBit.render('Start', False, (0, 0, 0))
	screen.blit(putin, (750,175))
	
	#First static die
	screen.blit(blankDie, (50,200))
	blankDieRect = blankDie.get_rect()
	dieX = blankDieRect.centerx
	dieY = blankDieRect.centery
	pg.draw.circle(blankDie, (0,0,0),(dieX,dieY),15, 0)
	
	## Second Static Die
	screen.blit(blankDie2, (150,275))
	
	pg.draw.rect(screen, (0,225,0), (450,450,300,100), 0)
	
	screen.blit(titleText,(0,0))
	if (mouseX > 450 and mouseX < 850) and (mouseY > 450 and mouseY < 550):
		
		#draw green start box
		pg.draw.rect(screen, (0,255,0), (450,450,300,100), 0)
		
	screen.blit(startText,(455,455))
	
###################################################
## Old Functions saving to see if can salvage    ##
###################################################
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
