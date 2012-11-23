# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729
# 
# Note: Internal methods use the array format starting at [0][0]
# 		A few interface methods use the format starting at A1:
#		PlaceSymbol(player, column, row), IsLegal(column, row)
# 		and GetIndex(column, row) which converts to the internal format


import os
import math
from Constants import *
from copy import deepcopy

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
	
class GameBoard:
	#initializer
	def __init__(self, board=None):
		if board:
			self.gameSpace = deepcopy(board.gameSpace)
		else:
			self.gameSpace = [[EMPTY_CELL_VALUE for j in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
		
	#output the board to console	
	def Print(self):
		cls()
		if VERBOSE:
			print("Printing board")
		row = ""
		for j in range(BOARD_WIDTH):
			row = row + '\t' + self.IntToLetter(j)
		print(row)
		for i in range(BOARD_HEIGHT):
			row = str(i + 1)
			for j in range(BOARD_WIDTH):
				row = row + '\t' + self.gameSpace[i][j]
			print(row)
	
	#Place a character in a specific square (using A1 format)
	def PlaceSymbol(self, player, column, row):
		(column, row) = self.GetIndex(column, row)
		self.gameSpace[row][column] = PLAYER_SYMBOLS[player]

	#Checks for a winner:
	# 1 : Player 1 wins
	# 2 : Player 2 wins
	# 0 : End of game, no winner
	#-1 : Game continues
	def CheckWinner(self):
		for i in range(BOARD_HEIGHT - BRIDGE_SIZE + 1):
			for j in range(BOARD_WIDTH - BRIDGE_SIZE + 1):
				winner = self.CheckWinColumn(i, j)
				if winner > 0:
					return winner
				winner = self.CheckWinRow(i, j)
				if winner > 0:
					return winner
				winner = self.CheckWinDiagDown(i, j)
				if winner > 0:
					return winner
				#checking 3rd quartile here instead of 1st
				winner = self.CheckWinDiagUp(i , j + BRIDGE_SIZE - 1)
				if winner > 0:
					return winner
		if self.IsDraw():
			return 0
		return -1
	
	#Check for a vertical win starting at position
	def CheckWinColumn(self, column, row):
		player = self.GetPlayer(column, row)
		if player <= 0:
			return -1
		for i in range(1, BRIDGE_SIZE):
			if self.IsOutOfBounds(column, row + i):
				return -1
			if self.gameSpace[row + i][column] is not PLAYER_SYMBOLS[player]:
				return -1
		return player
	
	#Check for a horizontal win starting at position
	def CheckWinRow(self, column, row):
		player = self.GetPlayer(column, row)
		if player <= 0:
			return -1
		for i in range(1, BRIDGE_SIZE):
			if self.IsOutOfBounds(column + i, row):
				return -1
			if self.gameSpace[row][column + i] is not PLAYER_SYMBOLS[player]:
				return -1
		return player
		
	#Check for a diagonal down (\) win starting at postion
	def CheckWinDiagDown(self, column, row):
		player = self.GetPlayer(column, row)
		if player <= 0:
			return -1
		for i in range(1, BRIDGE_SIZE):
			if self.IsOutOfBounds(column + i, row + i):
				return -1
			if self.gameSpace[row + i][column + i] is not PLAYER_SYMBOLS[player]:
				return -1
		return player
		
	#Check for a diagonal up (/) win starting at postion
	def CheckWinDiagUp(self, column, row):
		player = self.GetPlayer(column, row)
		if player <= 0:
			return -1
		for i in range(1, BRIDGE_SIZE):
			if self.IsOutOfBounds(column + i, row - i):
				return -1
			if self.gameSpace[row - i][column + i] is not PLAYER_SYMBOLS[player]:
				return -1
		return player
		
	#Get the id of the player who is at position
	def GetPlayer(self, column, row):
		for player in PLAYER_SYMBOLS.keys():
			if self.gameSpace[row][column] is PLAYER_SYMBOLS[player]:
				return player
		return -1
	
	# Checks for draw condition: no empty cell remaining
	def IsDraw(self):
		for i in range(BOARD_HEIGHT):
			for j in range(BOARD_WIDTH):
				if self.gameSpace[i][j] is EMPTY_CELL_VALUE:
					return False
		return True

	#Checks if the space is a legal move, testing all conditions (using A1 format)
	def IsLegal(self, column, row):
		(oldColumn, oldRow) = (column, row)
		(column, row) = self.GetIndex(column, row)
		if self.IsOutOfBounds(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(oldColumn), str(oldRow), "out of bounds.")
			return False
		if self.IsOccupied(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(oldColumn), str(oldRow), "occupied.")
			return False
		if not self.IsStacked(column, row):
			if VERBOSE:
				print("ILLEGAL MOVE:", str(oldColumn), str(oldRow), "not stacked")
			return False
		return True

	#Checks if space is already occupied, returns true if occupied else, returns false
	def IsOccupied(self, column, row):
		selectedSymbol = self.gameSpace[row][column]
		if selectedSymbol is EMPTY_CELL_VALUE:
			return False
		return True

	#Checks that input corresponds to a cell inside the Game Board
	def IsOutOfBounds(self, column, row):
		if int(column) not in range(BOARD_HEIGHT):
			return True
		if int(row) not in range(BOARD_WIDTH):
			return True
		return False

	#Verifies if the space is stacked on a wall or another brick
	def IsStacked(self, column, row):
		if self.IsOutOfBounds(column + 1, row) or self.IsOutOfBounds(column - 1, row):
			return True
		if self.IsOccupied(column + 1, row) or self.IsOccupied(column - 1, row):
			return True
		return False

	#Converts the column and row into array indexes (using A1 format)
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
		self.gameSpace = [[EMPTY_CELL_VALUE for j in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]
				
	def PopulateForTest(self, setting):
		if setting == 1: #check column
			self.gameSpace[0][0] = PLAYER_SYMBOLS[1]
			self.gameSpace[1][0] = PLAYER_SYMBOLS[1]
			self.gameSpace[2][0] = PLAYER_SYMBOLS[1]
			self.gameSpace[3][0] = PLAYER_SYMBOLS[1]
		if setting == 2: #check row
			self.gameSpace[0][0] = PLAYER_SYMBOLS[1]
			self.gameSpace[0][1] = PLAYER_SYMBOLS[1]
			self.gameSpace[0][2] = PLAYER_SYMBOLS[1]
			self.gameSpace[0][3] = PLAYER_SYMBOLS[1]
		if setting == 3: #check diagonal down
			self.gameSpace[0][0] = PLAYER_SYMBOLS[1]
			self.gameSpace[1][1] = PLAYER_SYMBOLS[1]
			self.gameSpace[2][2] = PLAYER_SYMBOLS[1]
			self.gameSpace[3][3] = PLAYER_SYMBOLS[1]
			
			self.gameSpace[4][0] = PLAYER_SYMBOLS[2]
			self.gameSpace[4][1] = PLAYER_SYMBOLS[2]
			self.gameSpace[4][2] = PLAYER_SYMBOLS[2]
			self.gameSpace[4][3] = PLAYER_SYMBOLS[2]
			
		if setting == 4: #check diagonal up
			self.gameSpace[4][3] = PLAYER_SYMBOLS[1]
			self.gameSpace[5][2] = PLAYER_SYMBOLS[1]
			self.gameSpace[6][1] = PLAYER_SYMBOLS[1]
			self.gameSpace[7][0] = PLAYER_SYMBOLS[1]
			
			self.gameSpace[3][0] = PLAYER_SYMBOLS[2]
			self.gameSpace[3][1] = PLAYER_SYMBOLS[2]
			self.gameSpace[3][2] = PLAYER_SYMBOLS[2]
			self.gameSpace[3][3] = PLAYER_SYMBOLS[2]
