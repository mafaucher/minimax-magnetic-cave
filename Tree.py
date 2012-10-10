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

	def AddNode(self, node):
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

	def RemoveNode(self, nodeId):
		tempNode = GetNode(nodeId)
		if not tempNode is None:
			self.list[tempNode.parentId].children.remove(tempNode.id)
			self.list.remove(tempNode)
		
	def HasLeftSibling(self, node):
		if self.list[node.parentId] is None:
			return false
		#use the index 
		
	def PreorderTraversal(self, node):
		if node is None:
			return
		
		print(node)
		#if len(node.children) > 0:
			

##### TEST #####
#test list based on the tree from assignment 2
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
tree.AddNode(node0)
tree.AddNode(node1)
tree.AddNode(node2)
tree.AddNode(node3)
tree.AddNode(node4)
tree.AddNode(node5)
tree.AddNode(node6)
tree.AddNode(node7)
tree.AddNode(node8)
tree.AddNode(node9)
tree.AddNode(node10)

for node in tree.list:
	print(node)

