# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

import os

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

#Game constants
BOARD_WIDTH = 8
BOARD_HEIGHT = 8

EMPTY_CELL_VALUE = '_'
PLAYER_SYMBOLS = { 1:'O', 2:'X' }

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
				row = row + '\t' + self.gameSpace[i][j]
			print(row)
	
	#Place a character in a specific square
	def PlaceSymbol(self, player, column, row):
		row = row - 1
		column = self.LetterToInt(column) - 1
		self.gameSpace[row][column] = PLAYER_SYMBOLS[player]

	#Checks if space is already occupied, returns true if occupied else, returns false
	def IsOccupied(self, column, row):
		row = row - 1
		column = self.LetterToInt(column) - 1
		selectedSymbol = self.gameSpace[row][column]
		if selectedSymbol == EMPTY_CELL_VALUE:
			return False
		else:
			return True

	#used to convert a character to an integer value that can be used in the 2D array
	#doesn't check bounds for now ...
	def LetterToInt(self, letter):
		letter = letter.upper()
		intchar = ord(letter) - 64
		return intchar
		
	#zeros out the board
	def ClearOutBoard(self):
		for i in range(BOARD_HEIGHT):
			for j in range(BOARD_WIDTH):
				self.gameSpace[i][j] = EMPTY_CELL_VALUE
