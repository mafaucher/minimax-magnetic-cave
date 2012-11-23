# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

VERBOSE = True

# Game Board

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

EMPTY_CELL_VALUE = '_'
PLAYER_SYMBOLS = { 1:'O', 2:'X' }
BRIDGE_SIZE = 5

# Heuristic Weights

WEIGHTS = {
		"11": 2,
		"12": 4,
		"13": 8,
		"14": 16,
		"15": 1000,
		"21":-2,
		"22":-4,
		"23":-8,
		"24":-16,
		"25":-1000,
		}

# Minimax

MAX_DEPTH = 3
MIN_H = 0
MAX_H = 40

# Test Tree (To demo Minimax)

TOTAL_DEPTH = 5
NUM_CHILDREN = 16
