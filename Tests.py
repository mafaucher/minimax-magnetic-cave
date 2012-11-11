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

node0 = Node('A')
node1 = Node('B')
node2 = Node('C')
node3 = Node('D')
node4 = Node('E')
node5 = Node('F')
node6 = Node('G')
node7 = Node('H')
node8 = Node('I')
node9 = Node('J')
node10 = Node('K')

tree = Tree()

print("============================")
print("  TESTS - PHASE 1  ")
print("============================")
print()
print("  TEST 1 - A Simple Tree")
print("============================")
tree.AddNode(node0, None)
tree.AddNodeById(node1, 'A')
tree.AddNodeById(node2, 'A')
tree.AddNodeById(node3, 'A')
tree.AddNodeById(node4, 'B')
tree.AddNodeById(node5, 'B')
tree.AddNodeById(node6, 'B')
tree.AddNodeById(node7, 'C')
tree.AddNodeById(node8, 'C')
tree.AddNodeById(node9, 'D')
tree.AddNodeById(node10, 'D')
print("============================")
print()
print("  TEST 2 - Iteration")
print("============================")
for node in tree:
	sys.stdout.write(node.id + " ")
print()
print("============================")
print()
print("  TEST 3 - H(n) (depricated)")
print("============================")
print("H(Leaves):")
for node in [n for n in tree if n.IsLeaf()]:
	print(node.id, '=', node.hScore)
print("============================")
print()
print("  TEST 4 - Level 1 nodes")
print("============================")
print("H(Height==1):")
for node in [n for n in tree if n.GetHeight() == 1]:
	print(node.id, '=', node.GetHeight())
print("==================")
print()
print("  TEST 5 - Adding Nodes")
print("============================")
node11 = Node('L')
tree.AddNodeById(node11, 'E')
print("reiteration after adding a node to E:")
for node in tree:
	print(node.id, end=" ")
print()
print("============================")
print()

print("  TEST 6 - Minimax")
print("============================")

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

userInput = "c"
while( userInput == "c" and not tree.root.IsLeaf() ):
	print()
	path = Minimax(tree)
	tree.root = path
	print("Winning path is to Node", tree.root.id)
	userInput = input("Press ENTER to exit, or 'c' to continue > ")
print()
print("============================")
print()
print("============================")
print("  TESTS - PHASE 2  ")
print("============================")
print()
print("  TEST 1 - Printing Board")
print("============================")
input()
#PlaceSymbol(self, player, column, row):
gameBoard.PlaceSymbol(1, 'a', 1)
gameBoard.PlaceSymbol(2, 'h', 2)
gameBoard.Print()

print()
print("  TEST 2 - Legal Moves")
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
