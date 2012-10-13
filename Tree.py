# Jonathan Bergeron, id : 9764453

from Node import Node
from NodeIterator import NodeIterator

class Tree:
	#initializer
	def __init__(self):
		self.root = None
	
	#creates a nodeIterator and traverses the tree
	def __iter__(self):
		nodeIterator = NodeIterator(self.root)
		return iter(nodeIterator)

	#adds a node to the tree
	def AddNode(self, node, parentId):
		if self.root is None:
			if parentId is None:
				self.root = node
				print(str(node.id) + " has parent: none and has height: " + str(node.GetHeight()))
			return
			
		parentNode = self.GetNode(parentId)
		if not parentNode is None:
			parentNode.children.append(node)
			node.parentNode = parentNode
			print(str(node.id) + " has parent: " + parentNode.id + " and has height: " + str(node.GetHeight()))

	#returns the node if it found it
	def GetNode(self, nodeId):		
		for node in self:
			if node.id == nodeId:
				return node

	#removes a node from the tree
	def RemoveNode(self, nodeId):
		tempNode = self.GetNode(nodeId)
		if tempNode is None:
			return
		#remove reference from parent
		tempNode.parentNode.children.remove(tempNode.id)
