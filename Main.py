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
	
#=============================================================================================

gameBoard = GameBoard()
playerAI = []

for i in range(2):
	question = "Will player ", str(i + 1), " be an AI player?"
	userInput = input(question)
	if userInput == "y":
		tempTree = Tree()
		if i % 2 == 0:
			tempTree.GenerateDepths(1)
		else:
			tempTree.GenerateDepths(2)
		playerAI.append(tempTree)
	else:
		playerAI.append(None)
		

currentPlayer = 1
score = { 1:0, 2:0 }
userInput = ""

# Multiple game loop
while userInput.lower() != "n":
	gameBoard.ClearOutBoard()
	firstPlayerPlayed = False  # only used once
	#gameBoard.PopulateForTest(4)
	# Main game loop
	
	#val = gameBoard.WeightedH(currentPlayer)
	#print("\nFINAL HEURISTIC:", val, "\n")
	#print("PLAYER", currentPlayer)
	
	while gameBoard.CheckWinner() < 0:
		if playerAI[currentPlayer - 1] is None: #human player
			gameBoard.Print()
			#gameBoard.GetNextAvailablePlays()
			print("\nPLAYER", currentPlayer, "\n")
		
			if firstPlayerPlayed:
				print("last move played: ", str(column), ", ", str(row))
			
			# Get legal coordinates
			(column, row) = GetCoord()
			while not gameBoard.IsLegal(column, row):
				print("Illegal input, try again.")
				(column, row) = GetCoord()
			
			gameBoard.PlaceSymbol(currentPlayer, column, row)
			
			nextPlayer = currentPlayer % 2 + 1
			tempNode = playerAI[nextPlayer - 1].GetNode(gameBoard)
			
			playerAI[nextPlayer - 1].SetRoot(tempNode)
			playerAI[nextPlayer - 1].GenerateDepths(nextPlayer)
			
		else: #AI player
			selectedNode = Minimax(playerAI[currentPlayer - 1], currentPlayer)
			column = selectedNode.gameBoard.moveColumn
			row = selectedNode.gameBoard.moveRow
			
			gameBoard.PlaceSymbol(currentPlayer, column, row)
			
			nextPlayer = currentPlayer % 2 + 1			
			
			#get ready for new move
			playerAI[currentPlayer - 1].SetRoot(selectedNode)
			playerAI[currentPlayer - 1].GenerateDepths(nextPlayer)
			
			firstPlayerPlayed = True # only used once
		

		# Switch current player
		currentPlayer = nextPlayer
	
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

