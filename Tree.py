# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *
from Node import Node
from NodeIterator import NodeIterator

class Tree:
	#initializer
	def __init__(self):
		self.root = None
		self.isDirty = False
		self.nodeIterator = None
	
	#creates a nodeIterator and traverses the tree
	def __iter__(self):
		if not self.nodeIterator or self.isDirty:
			self.nodeIterator = NodeIterator(self.root)
			self.isDirty = False
		else:
			self.nodeIterator.pos = 0
		return iter(self.nodeIterator)

	#adds a node without searching the tree
	def AddNode(self, node, parentNode=None, h=None):
		if not self.root:
			if not parentNode:
				self.root = node
				self.isDirty = True
				if VERBOSE:
					print(node.id, "has parent: none and has height:", node.GetHeight())
		elif parentNode:
			parentNode.children.append(node)
			node.parentNode = parentNode
			node.hScore = h
			self.isDirty = True
			if VERBOSE:
				print(node.id, "has parent:", parentNode.id, "and has height:", node.GetHeight())

	#adds a node to the tree by searching for parent ID
	def AddNodeById(self, node, parentId=None, h=None):
		if parentId:
			parentNode = self.GetNode(parentId)
		self.AddNode(node, parentNode, h)

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
