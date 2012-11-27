#!/usr/bin/python3


import os
import sys
from Constants import *
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard
from time import clock

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

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
	question = "Will player " + str(i + 1) + " be an AI player? (y/n) "
	userInput = input(question)
	if userInput == "y":
		playerAI.append("AI")
	else:
		playerAI.append(None)
		
numberOfGames = 1
currentPlayer = 1
score = { 1:0, 2:0 }
userInput = ""
timer = 0

# Multiple game loop
while userInput.lower() != "n":
	gameBoard.ClearOutBoard()
	
	for i in range(2):
		if playerAI[i]:
			playerAI[i] = Tree()
			playerAI[i].GenerateDepths(currentPlayer)
			
	column = None
	row = None

	# Main game loop
	while gameBoard.CheckWinner() < 0:	
		nextPlayer = currentPlayer % 2 + 1

		# Human player
		if not playerAI[currentPlayer - 1]: 
			# Output board and last move
			cls()
			gameBoard.Print()
			print("\nPLAYER", currentPlayer, "\n")
			if column:
				print("Last move played:", str(column)+str(row))
				if playerAI[nextPlayer - 1]:
					print("Played in:", round(timer, 2), "seconds")
				print()
			
			# Get legal coordinates
			(column, row) = GetCoord()
			while not gameBoard.IsLegal(column, row):
				print("Illegal input, try again.")
				(column, row) = GetCoord()
			
			gameBoard.PlaceSymbol(currentPlayer, column, row)
			
			# Playing against an AI
			if playerAI[nextPlayer - 1]:
				tempNode = playerAI[nextPlayer - 1].GetNode(gameBoard)
				playerAI[nextPlayer - 1].SetRoot(tempNode)
				playerAI[nextPlayer - 1].GenerateDepths(nextPlayer)

		# AI player
		else: 
			# Start the clock
			start = clock()

			# Minimax
			selectedNode = Minimax(playerAI[currentPlayer - 1], currentPlayer)
			gameBoard = GameBoard(selectedNode.gameBoard)
			column = selectedNode.gameBoard.moveColumn
			row = selectedNode.gameBoard.moveRow
			
			# Get ready for new move
			playerAI[currentPlayer - 1].SetRoot(selectedNode)
			playerAI[currentPlayer - 1].GenerateDepths(nextPlayer)

			# Stop the clock
			timer = clock() - start

			# Playing against an AI
			if playerAI[nextPlayer - 1]: 
				tempNode = playerAI[nextPlayer - 1].GetNode(gameBoard)
				playerAI[nextPlayer - 1].SetRoot(tempNode)
				playerAI[nextPlayer - 1].GenerateDepths(nextPlayer)

		# Switch current player
		currentPlayer = nextPlayer
	# Output final board
	cls()
	gameBoard.Print()
	print("\nLast move played:", str(column)+str(row))

	# Check winner and display score
	winner = gameBoard.CheckWinner()
	print("\nGAME OVER: ", end="")
	if winner is 0:
		print("IT'S A DRAW!")
	else:
		score[winner] += 1
		if playerAI[winner - 1]:
			print("PLAYER", winner, "(AI) WINS!")
		else:
			print("PLAYER", winner, "(HUMAN) WINS!")
	print()
	for player in score.keys():
		print("Player", player, ":", score[player])
	print()

	userInput = input("Play another game? (y/n) ")

	# Alternate between starting players
	numberOfGames += 1
	currentPlayer = 1 if numberOfGames % 2 else 2
