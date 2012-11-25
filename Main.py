#!/usr/bin/python3

import sys
from Constants import *
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard

#Prompt the user for input until valid coordinates are entered
def GetCoord():
	column = None
	row = None
	while not column or not row:
		try:
			coord = input("Enter your coordinates: ")
			column = coord[0]
			row = int(coord[1])
		except (ValueError, IndexError) as e:
			if VERBOSE:
				print(e)
			column = None
			row = None
	
	return (column, row)
	
	
gameBoard = GameBoard()
playerAI = []

for i in range(2):
	question = "Will player ", str(i + 1), " be an AI player?"
	userInput = input(question)
	if userInput == "y":
		playerAI.append(True)
	else:
		playerAI.append(False)

currentPlayer = 1
score = { 1:0, 2:0 }
userInput = ""

# Multiple game loop
while userInput.lower() != "n":
	gameBoard.ClearOutBoard()
	movePlayed = False
	#gameBoard.PopulateForTest(4)
	# Main game loop
	
	#val = gameBoard.WeightedH(currentPlayer)
	#print("\nFINAL HEURISTIC:", val, "\n")
	#print("PLAYER", currentPlayer)
	
	while gameBoard.CheckWinner() < 0:
		if not playerAI[currentPlayer - 1]: #human player
			gameBoard.Print()
			#gameBoard.GetNextAvailablePlays()
			print("\nPLAYER", currentPlayer, "\n")
		
			if movePlayed:
				print("last move played: ", str(column), ", ", str(row))
			
			# Get legal coordinates
			(column, row) = GetCoord()
			while not gameBoard.IsLegal(column, row):
				print("Illegal input, try again.")
				(column, row) = GetCoord()
		#else: #AI player
		
			gameBoard.PlaceSymbol(currentPlayer, column, row)
		movePlayed = True

		# Switch current player
		currentPlayer = currentPlayer % 2 + 1
	
	# Check winner and display score
	winner = gameBoard.CheckWinner()
	if winner is 0:
		print("It's a draw!")
	else:
		score[winner] += 1
	print()
	for player in score.keys():
		print("Player", player, ":", score[player])
	print()

	userInput = input("Play another game? (y/n) ")

