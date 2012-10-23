#!/usr/bin/python3

import sys
from Node import Node
from Tree import Tree
from Minimax import *

TOTAL_DEPTH = 4
NUM_CHILDREN = 2

count = 0

tree = Tree()
tree.AddNode(Node(count))
nodeList = [tree.root]

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
