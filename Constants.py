# Jonathan Bergeron, id : 9764453
# Marc-Andre Faucher,id : 9614729

VERBOSE = False

# Game Board

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

EMPTY_CELL_VALUE = '_'
PLAYER_SYMBOLS = { 1:'O', 2:'X' }
BRIDGE_SIZE = 5

# Minimax
MAX_DEPTH = 3
MIN_H = -1000
MAX_H = 1000

# Heuristic Weights

WEIGHTS = {
		"11": 1,
		"12": 4,
		"13": 16,
		"14": 64,
		"15": MAX_H,
		"21":-1,
		"22":-4,
		"23":-16,
		"24":-64,
		"25": MIN_H,
		}
