# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *

class Node:
	#initializer
	def __init__(self, nodeId=0, nodeHeight=-1):
		self.id = nodeId
		self.parentNode = None
		self.children = [] #for storing child nodes
		self.height = nodeHeight
		self.hScore = None
	
	def GetHeight(self):
		if self.height is -1:
			if self.parentNode:
				self.height = self.parentNode.GetHeight()+1
			else:
				self.height = 0
		return self.height
	
	#return true if the node is a leaf node. If false, then the node is an internal node
	def IsLeaf(self):
		if len(self.children) > 0:
			return False
		return True
