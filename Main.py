#!/usr/bin/python3

import sys
from Node import Node
from Tree import Tree
from Minimax import *

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

print("==================")
print(" TESTS - PHASE 1  ")
print("==================")
print()
print("  TEST 1")
print("==================")
print("Nodes in the tree:")
tree.AddNode(node0, None)
tree.AddNode(node1, 'A')
tree.AddNode(node2, 'A')
tree.AddNode(node3, 'A')
tree.AddNode(node4, 'B')
tree.AddNode(node5, 'B')
tree.AddNode(node6, 'B')
tree.AddNode(node7, 'C')
tree.AddNode(node8, 'C')
tree.AddNode(node9, 'D')
tree.AddNode(node10, 'D')
print("==================")
print()
print("  TEST 2")
print("==================")
print("Iteration:")
for node in tree:
	sys.stdout.write(node.id + " ")
print()
print("==================")
print()
print("  TEST 3")
print("==================")
print("H(Leaves):")
#for node in [n for n in tree if n.IsLeaf()]:
#	print(node.id, '=', node.hScore)
print("Minimax result =", MinimaxR(tree.root))
print("==================")
print()
print("  TEST 4")
print("==================")
print("H(Height==1):")
#for node in [n for n in tree if n.GetHeight() == 1]:
#	print(node.id, '=', node.hScore)
print("Minimax result =", MinimaxR(tree.root,depth=1))
print("==================")
print()
print("  TEST 5")
print("==================")
print()
node11 = Node('L')
tree.AddNode(node11, 'E')
print("reiteration after adding a node to E:")
for node in tree:
	print(node.id, end=" ")
print()
print("==================")
print()

#for node in [n for n in tree]
	
print(node10.GetHeight())
