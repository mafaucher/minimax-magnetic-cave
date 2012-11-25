#!/usr/bin/python3

import sys
from Constants import *
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard

def OtherPlayer(player):
	return player % 2 + 1

player = 1
gameBoard = GameBoard()

# Generate new trees for each AI
trees = {1 : Tree(), 2 : Tree()}
trees[1].GenerateDepths()
trees[2].GenerateDepths()
print(trees[1].CountNodes(), trees[2].CountNodes())
gameBoard.Print()

while True:
	otherPlayer = OtherPlayer(player)

	gameBoard.Print()
	print("Player", player, "will play next")
	print("Player 1:", gameBoard.WeightedH(1), "- Player 2:", gameBoard.WeightedH(2))
	input()

	# Select the best path according to Minimax and update current player's tree
	move = Minimax(trees[player], player)
	trees[player].SetRoot(move)

	# Update the main board by copying it from the current player's tree
	gameBoard = GameBoard(trees[player].root.gameBoard)
	
	# Update the other player's tree according to the move the current player just played
	tempNode = trees[otherPlayer].GetNode(gameBoard)
	trees[otherPlayer].SetRoot(tempNode)

	# Generate new depths for this both player's trees
	# NOTE: Remember to pass GenerateDepths the player which should be at the top of the tree
	#		In this case, this is the player who's turn it will be next.
	trees[player].GenerateDepths(otherPlayer)
	trees[otherPlayer].GenerateDepths(otherPlayer)

	# Switch Player
	player = otherPlayer
	
	winner = gameBoard.CheckWinner()
	if winner is 0:
		print("It's a draw!")
		break
	if winner is 1:
		print("Player 1 wins!")
		break
	if winner is 2:
		print("Player 2 wins!")
		break
	# NOTE: This Test does not check for winners, so expect an error when the game ends
