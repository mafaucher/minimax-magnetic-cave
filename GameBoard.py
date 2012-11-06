# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

import os

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

TAB = "\t"

#Game constants

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

EMPTY_CELL_VALUE = '_'
PLAYER1_CELL_VALUE = 'O'
PLAYER2_CELL_VALUE = 'X'

class GameBoard:
	#initializer
	def __init__(self):
		self.gameSpace = []
		
		for i in range(BOARD_HEIGHT):
			self.gameSpace.append([])
			for j in range(BOARD_WIDTH):
				self.gameSpace[i].append(EMPTY_CELL_VALUE)

	#output the board to console	
	def Print(self):
		cls()
		print("Printing board")
		for i in range(BOARD_HEIGHT):
			row = ""
			for j in range(BOARD_WIDTH):
				row = row + TAB + self.gameSpace[i][j]
			print(row)
	
	#zeros out the board
	def ClearOutBoard(self):
		for i in range(BOARD_HEIGHT):
			for j in range(BOARD_WIDTH):
				self.gameSpace[i][j] = EMPTY_CELL_VALUE