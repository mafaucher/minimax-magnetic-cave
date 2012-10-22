# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Node import Node
from Tree import Tree
from random import randrange

MAX_DEPTH = 3 # Maximum depth of minimax search
MIN_H = -400 # Minimum heuristic score
MAX_H =  400 # Maximum heuristic score

def Heuristic(node):
	val = randrange(0,MAX_H) # TODO: real heuristic score
	print("Explored Leaf", node.id, "with score", val)
	return val

def Maxi(node, depth=MAX_DEPTH):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node), None)
	max = MIN_H
	path = None
	for child in node.children:
		score = Mini(child, depth-1)[0]
		if score > max:
			path = child
			max = score
	return (max, path)

def Mini(node, depth=MAX_DEPTH):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node), None)
	min = MAX_H
	path = None
	for child in node.children:
		score = Maxi(child, depth-1)[0]
		if score < min:
			min = score
	return (min, path)

#def Minimax(node, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H, isMax=True):
#	path = None
#	if node.IsLeaf() or depth <= 0:
#		val = Heuristic(node)
#		print("Explored Leaf", node.id, "with score", val)
#		if isMax:
#			return (val, None)
#		else:
#			return (-val, None)
#	else:
#		for child in node.children:
#			val = Minimax(child, depth-1, -beta, -alpha, not isMax)[0]
#			val = -val
#			if val >= beta:
#				print("Set", node.id, "to", abs(val))
#				#path = child
#				return (val, child)
#			if val >= alpha:
#				path = child
#				alpha = val
#		print("Set Node", node.id, "to", abs(alpha))
#		return (alpha, path)

