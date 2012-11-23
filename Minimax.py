# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *
from Node import Node
from Tree import Tree
from GameBoard import GameBoard

def Heuristic(node, player):
	val = node.gameBoard.WeightedH(player)
	if VERBOSE:
		print("Explored Leaf", node.id, "with score", val)
	return val

def Minimax(tree, player, depth=MAX_DEPTH):
	(score, path) = Maxi(tree.root, player, depth)
	return path

def Maxi(node, player, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node, player), None)
	path = None
	for child in node.children:
		score = Mini(child, player, depth-1)[0]
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

def Mini(node, player, depth=MAX_DEPTH, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node, player), None)
	path = None
	for child in node.children:
		score = Maxi(child, player, depth-1)[0]
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
