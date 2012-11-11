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

currentPlayer = 1
score = { 1:0, 2:0 }
userInput = ""

# Multiple game loop
while userInput.lower() != "n":
	gameBoard.ClearOutBoard()

	# Main game loop
	while gameBoard.CheckWinner() < 0:
		gameBoard.Print()
		print()
		print("PLAYER", currentPlayer)
		print()

		# Get legal coordinates
		(column, row) = GetCoord()
		while not gameBoard.IsLegal(column, row):
			print("Illegal input, try again.")
			(column, row) = GetCoord()

		gameBoard.PlaceSymbol(currentPlayer, column, row)
		if currentPlayer is 1:
			currentPlayer = 2
		else:
			currentPlayer = 1

	# Check winner and display score
	winner = gameBoard.CheckWinner()
	if winner is 0:
		"It's a draw!"
	else:
		score[winner] += 1
	print()
	for player in score.keys():
		print("Player", player, ":", score[player])
	print()

	userInput = input("Play another game? (y/n) ")
