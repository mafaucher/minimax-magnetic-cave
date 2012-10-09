# Jonathan Bergeron, id : 9764453
# Inspired by the dictionary technique publicized by: http://blog.adambachman.org/2008/06/simple-tree-using-python-dictionary.html

class Node:

	def __init__(self, iden, p):
		self.id = iden
		self.parentId = p
		self.children = [] #store the childrens' ids


class Tree:

	def __init__(self):
		self.root = None
		self.list = {} #init empty dictionary

	def GetNode(self, iden):
		if iden in self.list:
			return self.list[iden]
		else:
			return None

	def Add(self, node):
		if self.root is None:
			if node.parentId is None:
				self.root = node
			else:
				return
		
		#if the node id is not taken, add the node
		if not node in self.list:
			self.list[node.id] = node

			parentNode = self.GetNode(node.parentId)
			if not parentNode is None:
				parentNode.children.append(node.id)
			else:
				return
		else:
			#replace the values of the node
			self.list[node.id].id = node.id
			self.list[node.id].children = node.children

	def Remove(self, nodeId):
		tempNode = GetNode(nodeId)
		if not tempNode is None:
			self.list[tempNode.parentId].children.remove(tempNode.id)
			self.list.remove(tempNode)



##### TEST #####
#test list based on the one from assignment 2


node0 = Node('A', None)
node1 = Node('B', 'A')
node2 = Node('C', 'A')
node3 = Node('D', 'A')
node4 = Node('E', 'B')
node5 = Node('F', 'B')
node6 = Node('G', 'B')
node7 = Node('H', 'C')
node8 = Node('I', 'C')
node9 = Node('J', 'D')
node10 = Node('K', 'D')

tree = Tree()
tree.Add(node0)
tree.Add(node1)
tree.Add(node2)
tree.Add(node3)
tree.Add(node4)
tree.Add(node5)
tree.Add(node6)
tree.Add(node7)
tree.Add(node8)
tree.Add(node9)
tree.Add(node10)

for node in tree.list:
	print(node)

