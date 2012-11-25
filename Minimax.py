# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

from Constants import *
from Node import Node
from Tree import Tree
from GameBoard import GameBoard

def Heuristic(node, player):
	return node.gameBoard.WeightedH(player)

def Minimax(tree, player, depth=MAX_DEPTH):
	(score, path) = Maxi(tree.root, player, depth)
	return path

def Maxi(node, player, depth, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node, player), None)
	path = None
	for child in node.children:
		score = Mini(child, player, depth-1)[0]
		if score >= beta:
			return (beta, path)
		if score > alpha:
			path = child
			alpha = score
	return (alpha, path)

def Mini(node, player, depth, alpha=MIN_H, beta=MAX_H):
	if node.IsLeaf() or depth <= 0:
		return (Heuristic(node, player), None)
	path = None
	for child in node.children:
		score = Maxi(child, player, depth-1)[0]
		if score <= alpha:
			return (alpha, path)
		if score < beta:
			path = child
			beta = score
	return (beta, path)
