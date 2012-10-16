# Jonathan Bergeron, id : 9764453

from Node import Node
from NodeIterator import NodeIterator

MAX_DEPTH = 3 # Maximum depth of minimax search
MIN_H = -40 # Minimum heuristic score
MAX_H =  40 # Maximum heuristic score

class Tree:
	#initializer
	def __init__(self):
		self.root = None
		self.isDirty = False
		self.nodeIterator = None
	
	#creates a nodeIterator and traverses the tree
	def __iter__(self):
		if self.isDirty:
			self.nodeIterator = NodeIterator(self.root)
			self.isDirty = False
		else:
			self.nodeIterator.pos = 0
		return iter(self.nodeIterator)

	#adds a node to the tree
	def AddNode(self, node, parentId):
		if not self.root:
			if not parentId:
				self.root = node
				self.isDirty = True
				print(str(node.id) + " has parent: none and has height: " + str(node.GetHeight()))
			return
			
		parentNode = self.GetNode(parentId)
		if parentNode:
			parentNode.children.append(node)
			node.parentNode = parentNode
			self.isDirty = True
			print(str(node.id) + " has parent: " + parentNode.id + " and has height: " + str(node.GetHeight()))

	#returns the node if it found it
	def GetNode(self, nodeId):		
		for node in self:
			if node.id == nodeId:
				return node

	#removes a node from the tree
	def RemoveNode(self, nodeId):
		tempNode = self.GetNode(nodeId)
		if not tempNode:
			return
		#remove reference from parent
		tempNode.parentNode.children.remove(tempNode.id)
		self.isDirty = True

	def Minimax(self, depth=MAX_DEPTH, node=None, alpha=MIN_H, beta=MAX_H, isMax=True):
		if node is None:
			node = self.root
		if node.IsLeaf() or not depth:
			if isMax:
				return node.hScore
			else:
				return -node.hScore
		else:
			for child in node.children:
				val = -self.Minimax(depth-1, child, -beta, -alpha, not isMax)
				if val >= beta:
					return val
				if val >= alpha:
					alpha = val
			return alpha
