class Node:
	#initializer
	def __init__(self, nodeId):
		self.id = nodeId
		self.parentNode = None
		self.children = [] #for storing child nodes
	
	#returns the height of the node.
	def GetNodeHeight(self):
		if IsRoot():
			return 0

		height = 1
		tempNode = parentNode

		while true:
			if not tempNode.parentNode is None:	
				height += 1
				tempNode = parentNode
			else:
				break
		return height
	
	#return is the node is a leaf node. If false, then the node is an internal node
	def IsLeaf(self):
		if len(self.children) > 0:
			return False
		return True

	#returns if the node is the root node
	def IsRoot(self):
		if parentNode is None:
			return True
		
		return False

