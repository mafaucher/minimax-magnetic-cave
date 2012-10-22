#!/usr/bin/python3

import sys
from Node import Node
from Tree import Tree
from Minimax import *

totalDepth = 6
numChildren = 2
count = 0

tree = Tree()
tree.AddNode(Node(count))
nodeList = [tree.root]

# Up to depth totalDepth, add numChildren nodes to each node
for depth in range(totalDepth):
	tempList = []
	for node in nodeList:
		for nthChild in range(numChildren):
			count += 1
			tempNode = Node(count)
			tree.AddNode(tempNode, node)
			tempList.append(tempNode)
	nodeList = tempList
print(count)

userInput = ""
while( userInput != "q" and not tree.root.IsLeaf() ):
	
	(val, path) = Maxi(tree.root)
	tree.root = path
	print("Winning path is to Node", tree.root.id, "with", val)
	userInput = input("Press ENTER to exit, or 'q' to quit > ")
