# Jonathan Bergeron, id : 9764453

class Node:
	#initializer
	def __init__(self, nodeId):
		self.id = nodeId
		self.parentNode = None
		self.hScore = -1 #will be used to store the heuristic score
		self.children = [] #for storing child nodes
	
	#returns the height of the node.
	def GetNodeHeight(self):
		height = 0
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
