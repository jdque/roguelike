import libtcodpy as libtcod

class Rect:
	def __init__(self, top, left, width, height):
		self.top = top
		self.left = left
		self.width = width
		self.height = height

class Tile:
    class __TileType:
        """Private enum for class tile
        floor = 0
        wall = 1
        """
        floor = 0
        wall = 1
	#a tile of the map and its properties
	def __init__(self, char, fg, bg, tileType):
		self.char = char
		self.fg = fg
		self.bg = bg
		self.tileType = tileType

	def set_char(self, char):
		self.char = char

	def set_fg(self, fg):
		self.fg = fg

	def set_bg(self, bg):
		self.bg = bg

	def set_type(self, type):
		self.type = type

class Map:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = [[Tile(0, libtcod.Color(0,0,0), libtcod.Color(0,0,0), 0)
			for y in range(self.height)]
				for x in range(self.width)]

	def draw(self, con):
		for y in range(self.height):
			for x in range(self.width):
				libtcod.console_put_char_ex(con, x, y, self.tiles[x][y].char, self.tiles[x][y].fg, self.tiles[x][y].bg)

	def set_tile(self, x, y, tile):
		self.tiles[x][y].set_char(tile.char)
		self.tiles[x][y].set_fg(tile.fg)
		self.tiles[x][y].set_bg(tile.bg)
		self.tiles[x][y].set_type(tile.type)

	def get_tile(self, x, y):
		return self.tiles[x][y]

	def fill(self, tile):
		for y in range(self.height):
			for x in range(self.width):
				self.tiles[x][y].set_char(tile.char)
				self.tiles[x][y].set_fg(tile.fg)
				self.tiles[x][y].set_bg(tile.bg)
				self.tiles[x][y].set_type(tile.type)