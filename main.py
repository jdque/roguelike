import libtcodpy as libtcod

SCREEN_WIDTH = 64
SCREEN_HEIGHT = 64
LIMIT_FPS = 20

MAP_WIDTH = 64
MAP_HEIGHT = 64

con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

class Object:
	#this is a generic object: the player, a monster, an item, the stairs...
	#it's always represented by a character on screen.
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		
	def move(self, dx, dy):
	
		#collision detection
		if not map[self.x + dx][self.y + dy].blocked:
			#move by the given amount
			self.x += dx
			self.y += dy
		
	def draw(self):
		#set the color and then draw the character that represents this object at its position
		libtcod.console_set_default_foreground(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
		
	def clear(self):
		#erase the character that represents this object
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
		
class Tile:
	#a tile of the map and its properties
	def __init__(self, blocked, block_sight = None):
		self.blocked = blocked
		#by default, if a tile is blocked, it also blocks sight
		if block_sight is None: block_sight = blocked
		self.block_sight = block_sight
	
		self.char = ''
		
	def set_char(char):
		self.char = char
		
def handle_keys():
	
	key = libtcod.console_check_for_keypress()
	
	if key.vk == libtcod.KEY_ENTER and key.lalt:
	#Alt+Enter: toggle fullscreen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
		
	elif key.vk == libtcod.KEY_ESCAPE:
		return True  #exit game
		
	#movement keys
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)

def render_all():
	#draw all objects in the list
	for object in objects:
		object.draw()
		
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET )
			if map[x][y].char:
				libtcod.console_put_char(con, x, y, map[x][y].char, libtcod.BKGND_NONE)	

			#wall = map[x][y].block_sight
			#if wall:
			#	libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET )
			#else:
			#	libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET )
	
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	
def make_map():
	global map
	
	#fill map with "unblocked" tiles
	map = [[ Tile(False)
		for y in range(MAP_HEIGHT) ]
			for x in range(MAP_WIDTH) ]

##########################		
#main loop initialization#
##########################

libtcod.console_set_custom_font('terminal8x8_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

#create objects

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 2, libtcod.white)
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
objects = [npc, player]

#create tiles

color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

#create map
			
make_map()
	
for i in range(1, MAP_HEIGHT-1):
	for j in range(1, MAP_WIDTH-1):
		if libtcod.random_get_int(False, 0, 100) < 45:
			map[i][j].blocked = True
			map[i][j].char = '#'

for k in range(4):
	for i in range(1, MAP_HEIGHT-1):
		for j in range(1, MAP_WIDTH-1):	
			count = 0
			if map[i][j].blocked == True:
				count += 1
			if map[i-1][j].blocked == True:
				count += 1
			if map[i-1][j+1].blocked == True:
				count += 1
			if map[i][j+1].blocked == True:
				count += 1
			if map[i+1][j+1].blocked == True:
				count += 1
			if map[i+1][j].blocked == True:
				count += 1
			if map[i+1][j-1].blocked == True:
				count += 1
			if map[i][j-1].blocked == True:
				count += 1
			if map[i-1][j-1].blocked == True:
				count += 1
				
			if map[i][j].blocked == False and count >= 5:
				map[i][j].char = '#'
			elif map[i][j].blocked == True and count >= 4:
				map[i][j].char = '#'

	for a in range(MAP_HEIGHT):
		for b in range(MAP_WIDTH):
			if map[a][b].char == '#':
				if map[a-1][b].blocked == False and map[a+1][b].blocked == False and map[a][b+1].blocked == False and map[a][b-1].blocked == False:
					map[a][b].char = ''
					map[a][b].blocked = False
				else:
					map[a][b].blocked = True
				
#main loop

while not libtcod.console_is_window_closed():
	render_all()
	libtcod.console_flush()
	for object in objects:
		object.clear()
		
	exit = handle_keys()
	if exit:
		break