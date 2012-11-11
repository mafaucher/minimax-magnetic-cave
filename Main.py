#!/usr/bin/python3

import sys
from Constants import *
from Node import Node
from Tree import Tree
from Minimax import *
from GameBoard import GameBoard

gameBoard = GameBoard()
gameBoard.PlaceSymbol(1, 'a', 1)
gameBoard.PlaceSymbol(2, 'h', 2)
gameBoard.Print()
