# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Node import Node
MAX_DEPTH = 3
class NodeIterator:
	
	#initializer
	def __init__(self, rootNode):
		self.nodeList = []
		self.pos = 0
		self.AddChildrenNodes(rootNode)
	
	#iterative reference
	def __iter__(self):
		return iter(self.nodeList)

	#gets the next node
	def next(self):
		if self.pos > len(self.nodeList) - 1:
			raise StopIteration
		
		tempNode = self.nodeList[self.pos]
		self.pos += 1
		return tempNode

	#recurse method used to build the list for the iteration.
	def AddChildrenNodes(self, node):
		for tempNode in node.children:
			self.AddChildrenNodes(tempNode)
		self.nodeList.append(node)
