# Classes to import
import random




# Main file for romainian dice
pocketMoney = 100
bet = 0
continueGame = True


def checkUserInput():
	userAnswer = input("\nDo you know the rules? (y/n)")

	if userAnswer.lower() == 'y':
		startGame()
	
	elif userAnswer.lower() == 'n':
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
	
	print("")
	print("Let's start the game!")
	
	
	
	
def takeBet():
	global pocketMoney
	global bet
	
	try: 
		print("\nCurrent money in your pocket $" + str(pocketMoney))
	
		bet = int(input("\nHow much would you like to bet?"))
	
		if bet <= 0:
			print("\nYou can't bet less than zero!")
			takeBet()
	
		elif bet > pocketMoney:
			print("\nYou can't bet more than what you have!")
			takeBet()
		
		elif bet > 0 and int(bet) <= pocketMoney:
			print("You have bet $" +  str(bet))
			pocketMoney -= bet
			print("\nRemaining money $" + str(pocketMoney))
		
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
	
	die1 = random.randint(1,6)
	print("\nThe die rolled is: " + str(die1))
	
	if selection == 1:
		if die1 % 2 != 0:
			print("You won!")
			winnings = (bet*2)
			pocketMoney += winnings 
			
		else:
			print("Sorry you lose your bet")
			
			
	elif selection == 2:
		if die1 % 2 == 0:
			print("You won!")
			winnings = (bet*2)
			pocketMoney += winnings 
			
		else:
			print("Sorry you lose your bet")		
			

# Start of the game 

startUpMessage = "Welcome to romanian dice game!"
startUpMessage += "\nThe safe and fun romanian dice game simulator"

print(startUpMessage)
checkUserInput()

while continueGame:
	takeBet()
	checkUserBets()
	
	if pocketMoney <= 0:
		continueGame = False
		
if continueGame = False:
	print("\n Looks like you lost all your money! Sucks!")
