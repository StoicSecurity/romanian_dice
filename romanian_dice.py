# Classes to import
import random
from player import Player
from die import Die

# Main file for romainian dice
pocketMoney = 100
bet = 0
continueGame = True
current_player = Player()

def gatherPlayerInfo():
	print("\nFirst we need some information about you...")
	try:
		startingCash = int(input("How much money do you have in your pocket?"))
		
	except ValueError:
		print("That can't be in your pocket")
		gatherPlayerInfo()
		
	name = input("Now we just need to know your name: ")
	
	current_player = Player(name, startingCash)
	
	print("Welcome, " + current_player.name + "\nYou have $" + str(current_player.starting_cash))
		

def checkUserInput():
	userAnswer = input("\n" + current_player.name.title() + " Do you know the rules? (y/n)")

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
	global bet
	
	try: 
		print("\nCurrent money in your pocket $" + str(current_player.starting_cash))
	
		bet = int(input("\nHow much would you like to bet?"))
	
		if bet <= 0:
			print("\nYou can't bet less than zero!")
			takeBet()
	
		elif bet > current_player.starting_cash:
			print("\nYou can't bet more than what you have!")
			takeBet()
		
		elif bet > 0 and int(bet) <= current_player.starting_cash:
			print("You have bet $" +  str(bet))
			current_player.starting_cash -= bet
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
			winnings = (bet*2)
			current_player.starting_cash += winnings 
			
		else:
			print("Sorry you lose your bet")
			
			
	elif selection == 2:
		if result % 2 == 0:
			print("You won!")
			winnings = (bet*2)
			current_player.starting_cash += winnings 
			
		else:
			print("Sorry you lose your bet")		
			
###############################################################################
# Start of the game 
###############################################################################
startUpMessage = "Welcome to romanian dice game!"
startUpMessage += "\nThe safe and fun romanian dice game simulator"

print(startUpMessage)

gatherPlayerInfo()
checkUserInput()

die_1 = Die()

while continueGame:
	takeBet()
	checkUserBets()
	
	if current_player.starting_cash <= 0:
		continueGame = False
		
	if continueGame == False:
		print("\n Looks like you lost all your money! Sucks!")
