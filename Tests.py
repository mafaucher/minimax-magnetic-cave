#!/usr/bin/python3

import sys
from Constants import *
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard

##Test list based on the tree from assignment 2:
#                  A
#          /       |       \
#          B       C       D
#        / | \   /   \   /   \
#       E  F  G  H   I   J   K

nodeA = Node()
nodeB = Node(nodeA)
nodeC = Node(nodeA)
nodeD = Node(nodeA)
nodeE = Node(nodeB)
nodeF = Node(nodeB)
nodeG = Node(nodeB)
nodeH = Node(nodeC)
nodeI = Node(nodeC)
nodeJ = Node(nodeD)
nodeK = Node(nodeD)

tree = Tree()
tree.AddNode(Node(), tree.root)
gameBoard = GameBoard()
"""
## GENERATE TREE ##

for depth in range(TOTAL_DEPTH):
	tempList = []
	for node in nodeList:
		for nthChild in range(NUM_CHILDREN):
			tempNode = Node()
			tree.AddNode(tempNode, node)
			tempList.append(tempNode)
	nodeList = tempList

## MINIMAX ##

userInput = "c"
while( userInput == "c" and not tree.root.IsLeaf() ):
	print()
	path = Minimax(tree)
	tree.root = path
	print("Winning path is to Node", tree.root.id)
	userInput = input("Press ENTER to exit, or 'c' to continue > ")
print()
print("============================")

gameBoard.PlaceSymbol(1, 'a', 1)
gameBoard.PlaceSymbol(2, 'h', 2)
gameBoard.Print()
print()
print("============================")
print("  TESTS - PHASE 2  ")
print("============================")
print()
print("  TEST 1 - Legal Moves")
print("============================")
print("checking for a1:")
if gameBoard.IsLegal('a', 1):
	print("Legal move")

print("checking for h9:")
if gameBoard.IsLegal('h', 9):
	print("Legal move")

print("checking for b6:")
if gameBoard.IsLegal('b', 6):
	print("Legal move")

print("checking for a2:")
if gameBoard.IsLegal('a', 2):
	print("Legal move")

if gameBoard.IsDraw():
	print("Draw")

gameBoard.PlaceSymbol(1, 'e', 1)
gameBoard.PlaceSymbol(1, 'd', 2)
gameBoard.PlaceSymbol(1, 'c', 3)
gameBoard.PlaceSymbol(1, 'b', 4)
gameBoard.PlaceSymbol(1, 'a', 5)

input()

gameBoard.Print()
print()
print("  TEST 2 - Winner")
print("============================")
winner = gameBoard.CheckWinner()
if winner is 1:
	print("Player 1, a winner is you!")
elif winner is 2:
	print("Player 2, a winner is you!")
elif winner is 0:
	print("Too bad, it's a draw")
else:
	print("No winner")
	"""
