# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *
from GameBoard import *

class Node:
	#initializer
	def __init__(self, parentNode=None):
		self.parentNode = parentNode
		if self.parentNode:
			board = self.parentNode.gameBoard
		else:
			board = None
		self.gameBoard = GameBoard(board)
		self.children = [] #for storing child nodes
		#self.hScore = None
	
	#return true if the node is a leaf node. If false, then the node is an internal node
	def IsLeaf(self):
		if len(self.children) > 0:
			return False
		return True
