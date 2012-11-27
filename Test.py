#!/usr/bin/python3

import sys
import time
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

start = time.clock()
trees[1].GenerateDepths()
timer = time.clock() - start
trees[2].GenerateDepths()
gameBoard.Print()
flag = False
turn = 1
while True:
	otherPlayer = OtherPlayer(player)

	gameBoard.Print()
	print("PLAYER", player, "- TURN", turn, "- DEPTH", MAX_DEPTH, "TREES: ", trees[1].CountNodes(), trees[2].CountNodes(), "\n-----------------")
	print("HEURISTIC:\nPlayer 1:", gameBoard.WeightedH(1), "- Player 2:", gameBoard.WeightedH(2))
	print("TIME:")
	print("Player", player, "- Time for new depth:", timer)
	
	# Select the best path according to Minimax and update current player's tree
	start = time.clock()
	move = Minimax(trees[player], player, MAX_DEPTH)
	elapsed = time.clock() - start
	timer += elapsed
	print("Player", player, "- Time for Minimax:", elapsed)
	print("Player", player, "- Total time:", timer)
	trees[player].SetRoot(move)

	# Update the main board by copying it from the current player's tree
	gameBoard = GameBoard(trees[player].root.gameBoard)
	
	# Update the other player's tree according to the move the current player just played
	tempNode = trees[otherPlayer].GetNode(gameBoard)
	trees[otherPlayer].SetRoot(tempNode)

	turn += 1

	# Generate new depths for this both player's trees
	# NOTE: Remember to pass GenerateDepths the player which should be at the top of the tree
	#		In this case, this is the player who's turn it will be next.
	start = time.clock()
	trees[player].GenerateDepths(otherPlayer, MAX_DEPTH)
	elapsed = time.clock() - start
	timer += elapsed
	print("Player", player, "- Time new depth:", elapsed, "(During other player's turn)")

	start = time.clock()
	trees[otherPlayer].GenerateDepths(otherPlayer, MAX_DEPTH)
	timer = time.clock() - start

	# Switch Player
	player = otherPlayer
	
	winner = gameBoard.CheckWinner()
	if winner is 0:
		gameBoard.Print()
		print("It's a draw!")
		break
	if winner is 1:
		print("Player 1 wins!")
		gameBoard.Print()
		break
	if winner is 2:
		print("Player 2 wins!")
		gameBoard.Print()
		break

	input("Press <ENTER> to continue: ")
