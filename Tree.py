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

	def SetRootAndExpand(self, node, possibleMoves):
		self.root = node
		node.parentNode = None
		