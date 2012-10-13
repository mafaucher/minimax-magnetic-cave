from Node import Node
from Tree import Tree

#test list based on the tree from assignment 2
node0 = Node('A')
node1 = Node('B')
node2 = Node('C')
node3 = Node('D')
node4 = Node('E')
node5 = Node('F')
node6 = Node('G')
node7 = Node('H')
node8 = Node('I')
node9 = Node('J')
node10 = Node('K')

tree = Tree()

tree.AddNode(node0, None)
tree.AddNode(node1, 'A')
tree.AddNode(node2, 'A')
tree.AddNode(node3, 'A')
tree.AddNode(node4, 'B')
tree.AddNode(node5, 'B')
tree.AddNode(node6, 'B')
tree.AddNode(node7, 'C')
tree.AddNode(node8, 'C')
tree.AddNode(node9, 'D')
tree.AddNode(node10, 'D')

for node in tree:
	print(node.id)
