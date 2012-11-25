# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *
from Node import Node

class Tree:
	#initializer
	def __init__(self):
		self.root = Node()

	#adds a node without searching the tree
	def AddNode(self, node, parentNode=None):
		node = Node(parentNode)

	def SetRoot(self, node):
		self.root = node
		node.parentNode = None
	
	# Find the node which corresponds to the player's move
	def GetNode(self, currentBoard):
		for child in self.root.children:
			if child.gameBoard == currentBoard:
				return child
		raise ValueError("Unpredicted Game Move")

	def GetNodeByMove(self, move, player):
		currentBoard = GameBoard(self.root.gameBoard, move, player)
		return self.GetNode(currentBoard)

	# For testing purposes only
	def CountNodes(self):
		count = 0
		nodeList = [self.root]
		for level in range(20):
			tempList = []
			if not nodeList:
				break
			for node in nodeList:
				count += 1
				tempList.extend(node.children)
			nodeList = tempList
		return count

	# Recursive method which returns all leaves starting at node or root
	def GetLeaves(self, node=None):
		leaves = []
		if not node:
			node = self.root
		# Return node if it is leaf
		if node.IsLeaf:
			return [node]
		# Or return leaves of children
		for child in node.children:
			leaves.extend(child.GetLeaves())
		return leaves

	# Makes sure the tree is generated up to MAX_DEPTH
	def GenerateDepths(self, player=1):
		nodeList = [self.root]
		for depth in range(MAX_DEPTH):
			otherPlayer = player % 2 + 1
			tempList = []
			for node in nodeList:
				if node.IsLeaf:
					# Get a list of available moves
					moves = node.gameBoard.GetNextAvailablePlays()
					# Add a node in the tree for each move
					for move in moves:
						tempList.append(Node(node, move, otherPlayer))
				else:
					tempList.extend(node.children)
			# Switch player
			player = otherPlayer
			nodeList = tempList
