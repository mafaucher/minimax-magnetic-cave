# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

import os
from Constants import *

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

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
		if VERBOSE:
			print("Printing board")
		row = ""
		for j in range(BOARD_WIDTH):
			row = row + '\t' + self.IntToLetter(j + 1)
		print(row)
		for i in range(BOARD_HEIGHT):
			row = str(i + 1)
			for j in range(BOARD_WIDTH):
				row = row + '\t' + self.gameSpace[i][j]
			print(row)
	
	#Place a character in a specific square
	def PlaceSymbol(self, player, column, row):
		(column, row) = self.GetIndex(column, row)
		self.gameSpace[row][column] = PLAYER_SYMBOLS[player]

	#Checks if the space is a legal move, testing all conditions
	def IsLegal(self, column, row):
		if self.IsOutOfBounds(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(column), str(row), "out of bounds.")
			return False
		if self.IsOccupied(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(column), str(row), "occupied.")
			return False
		if not self.IsStacked(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(column), str(row), "not stacked")
			return False
		return True

	#Checks if space is already occupied, returns true if occupied else, returns false
	def IsOccupied(self, column, row):
		(column, row) = self.GetIndex(column, row)
		selectedSymbol = self.gameSpace[row][column]
		if selectedSymbol == EMPTY_CELL_VALUE:
			return False
		return True

	#Checks that input corresponds to a cell inside the Game Board
	def IsOutOfBounds(self, column, row):
		if int(row) not in range(1, BOARD_WIDTH):
			return True
		if column.upper() not in map(chr, range(65, 65 + BOARD_HEIGHT)):
			return True
		return False

	#Verifies if the space is stacked on a wall or another brick
	def IsStacked(self, column, row):
		(tempColumn, tempRow) = self.GetIndex(column, row)
		leftColumn = self.IntToLetter(tempColumn - 1)
		rightColumn = self.IntToLetter(tempColumn + 1)
		if self.IsOutOfBounds(rightColumn, row) or self.IsOutOfBounds(leftColumn, row):
			return True
		if self.IsOccupied(rightColumn, row) or self.IsOccupied(leftColumn, row):
			return True
		return False

	#Converts the column and row into array indexes
	def GetIndex(self, column, row):
		row = int(row) - 1
		column = self.LetterToInt(column) - 1
		return (column, row)

	#used to convert a character to an integer value that can be used in the 2D array
	def LetterToInt(self, letter):
		letter = letter.upper()
		intchar = ord(letter) - 64
		return intchar

	#used to convert an integer value to a character used by the Game Board
	def IntToLetter(self, intchar):
		intchar = int(intchar)
		letter = chr(intchar + 65)
		return letter

	#zeros out the board
	def ClearOutBoard(self):
		for i in range(BOARD_HEIGHT):
			for j in range(BOARD_WIDTH):
				self.gameSpace[i][j] = EMPTY_CELL_VALUE
