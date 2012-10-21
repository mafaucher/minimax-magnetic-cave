# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Node import Node
from Tree import Tree
from random import randrange

MAX_DEPTH = 3 # Maximum depth of minimax search
MIN_H = -40 # Minimum heuristic score
MAX_H =  40 # Maximum heuristic score

def Heuristic(node):
	return randrange(0,20) # TODO: heuristic score

def Minimax(node, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H, isMax=True):
	if node.IsLeaf() or not depth:
		h = Heuristic(node)
		print(node.id, "=", h)
		if isMax:
			return h
		else:
			return -h
	else:
		for child in node.children:
			val = -Minimax(child, depth-1, -beta, -alpha, not isMax)
			if val >= beta:
				return val
			if val >= alpha:
				alpha = val
		return alpha
