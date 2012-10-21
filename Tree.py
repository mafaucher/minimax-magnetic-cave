# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

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
			print(node.id, "is child of", parentNode.id)
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
