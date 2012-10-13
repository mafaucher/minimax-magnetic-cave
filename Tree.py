# Jonathan Bergeron, id : 9764453

from Node import Node
from NodeIterator import NodeIterator

class Tree:
	#initializer
	def __init__(self):
		self.root = None
		self.nodeDictionary = {} #dictionary used for quick searches
	
	#creates a nodeIterator and traverses the tree
	def __iter__(self):
		nodeIterator = NodeIterator(self)
		return iter(nodeIterator)

	#adds a node to the tree and dictionary, if a node with the same id already exists, it will return
	def AddNode(self, node, parentId):
		#checks if the node reference of the tree points to None
		#if so, the new none must be a root node
		if self.root is None:
			if parentId is None:
				self.root = node
				self.nodeDictionary.update({node.id : node})
			return
		
		#if the node id is not taken, add the node
		if not node in self.nodeDictionary:
			self.nodeDictionary.update({node.id : node})
			
			parentNode = self.GetNode(parentId)
			if not parentNode is None:
				parentNode.children.append(node)
		

	#returns the node if it found it, else it returns None
	def GetNode(self, nodeId):
		tempNode = self.nodeDictionary[nodeId]
		
		if not tempNode is None:
			return tempNode
		else:
			return None

	#removes a node from the tree and the dictionary
	def RemoveNode(self, nodeId):
		tempNode = self.GetNode(nodeId)
		if tempNode is None:
			return

		#remove reference from parent
		tempNode.parentNode.children.remove(tempNode.id)
		self.nodeDictionary.remove(tempNode)
		self.wasModified = True

	#prints the tree
	def Print(self):
		for node in self.nodeDictionary:
			print(node)
