# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Node import Node
from Tree import Tree
from random import randrange

MAX_DEPTH = 3 # Maximum depth of minimumimax search
MIN_H = 0 # Minimum heuristic score
MAX_H = 40 # Maximum heuristic score
VERBOSE = True

def Heuristic(node):
	val = randrange(0,MAX_H) # TODO: real heuristic score
	if VERBOSE:
		print("Explored Leaf", node.id, "with score", val)
	return val

def Maxi(node, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node), None)
	path = None
	for child in node.children:
		score = Mini(child, depth-1)[0]
		if score >= beta:
			if VERBOSE:
				print("Beta pruning for", child.id, ":", score, ">=", beta)
			return (beta, path)
		if score > alpha:
			if VERBOSE:
				print("Updated Node (MAX)", node.id, "path to", child.id, ":", alpha, "->", score)
			path = child
			alpha = score
	return (alpha, path)

def Mini(node, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node), None)
	path = None
	for child in node.children:
		score = Maxi(child, depth-1)[0]
		if score <= alpha:
			if VERBOSE:
				print("Alpha pruning for", child.id, ":", score, "<=", alpha)
			return (alpha, path)
		if score < beta:
			if VERBOSE:
				print("Updated Node (MIN)", node.id, "path to", child.id, ":", beta, "->", score)
			path = child
			beta = score
	return (beta, path)

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

