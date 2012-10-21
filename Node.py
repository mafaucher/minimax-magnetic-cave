# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

class Node:
	#initializer
	def __init__(self, nodeId, nodeHeight=None):
		self.id = nodeId
		self.parentNode = None
		self.children = [] #for storing child nodes
		self.height = nodeHeight
	
	#returns the height of the node.
	def GetHeight(self):
		if not self.height:
			self.height = 0
			tempNode = self
		
			while tempNode.parentNode:
				self.height += 1
				tempNode = tempNode.parentNode

		return self.height
	
	#return if the node is a leaf node. If false, then the node is an internal node
	def IsLeaf(self):
		if len(self.children) > 0:
			return False
		return True
