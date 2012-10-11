# Jonathan Bergeron, id : 9764453

import copy
from Node import Node


class NodeIterator:

	def __init__(self, tree):
		self.tree = tree
		self.stack = []
		self.pos = 0
	
	def __iter__(self):
		return self

	def next(self):
		if self.tree is None or self.tree.root is None:			
			return

		self.pos += 1

		if self.tree.wasModified is True:

			self.tree.wasModified = False
			self.pos = 0
			self.stack = []
			self.stack.append(self.tree.root)
			
			for node in self.stack:
				#tempList = copy.deepcopy(node.children)
				#tempList.reverse()
				#self.stack += tempList
				self.stack += node.children

			#self.stack.reverse()

		if self.pos > len(self.stack) - 1:
			raise StopIteration
		
		#print(self.stack[self.pos])
		return self.stack[self.pos]
