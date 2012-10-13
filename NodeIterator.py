# Jonathan Bergeron, id : 9764453

from Node import Node

class NodeIterator:

	def __init__(self, tree):
		self.tree = tree
		self.nodeList = []
		self.pos = 0
		self.AddChildrenNodes(self.tree.root)
	
	def __iter__(self):
		return iter(self.nodeList)

	def next(self):
		if self.pos > len(self.nodeList) - 1:
			raise StopIteration
		
		tempNode = self.nodeList[self.pos]
		self.pos += 1
		return tempNode

	def AddChildrenNodes(self, node):
		for tempNode in node.children:
			self.AddChildrenNodes(tempNode)
		self.nodeList.append(node)
