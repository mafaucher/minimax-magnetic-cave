#!/usr/bin/python3

import sys
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard

TOTAL_DEPTH = 4
NUM_CHILDREN = 2

count = 0

tree = Tree()
tree.AddNode(Node(count))
nodeList = [tree.root]
gameBoard = GameBoard()


## GENERATE TREE ##

for depth in range(TOTAL_DEPTH):
	tempList = []
	for node in nodeList:
		for nthChild in range(NUM_CHILDREN):
			count += 1
			tempNode = Node(count)
			tree.AddNode(tempNode, node)
			tempList.append(tempNode)
	nodeList = tempList

## MINIMAX ##

userInput = ""
while( userInput != "q" and not tree.root.IsLeaf() ):
	print()
	(val, path) = Maxi(tree.root)
	tree.root = path
	print("Winning path is to Node", tree.root.id, "with", val)
	userInput = input("Press ENTER to exit, or 'q' to quit > ")

#PlaceSymbol(self, player, column, row):
gameBoard.PlaceSymbol(1, 'a', 1)
gameBoard.PlaceSymbol(2, 'h', 2)
gameBoard.Print()

print("checking if a1 is occupied")
print(gameBoard.IsOccupied('a', 1))

print("checking if h2 is occupied")
print(gameBoard.IsOccupied('h', 2))

print("checking if b6 is occupied")
print(gameBoard.IsOccupied('b', 6))
