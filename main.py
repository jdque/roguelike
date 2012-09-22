import libtcodpy as libtcod
from map import *
from map_generator import *

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

def render_all(objectList, map):
	#draw all objects in the list
	for object in objectList:
		object.draw()
	
	map.draw(con)
	
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

##########################		
#main loop initialization#
##########################

libtcod.console_set_custom_font('fonts/terminal8x8_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

#create objects

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 2, libtcod.white)
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
objects = [npc, player]

#create tiles

tile_wall = Tile(219, libtcod.Color(255,255,255), libtcod.Color(0,0,0), 1)
tile_floor = Tile(' ', libtcod.Color(0,0,0), libtcod.Color(0,0,0), 0)

#create map

map = Map(64,64)
map.fill(tile_floor)
cave(map)
			
#main loop

while not libtcod.console_is_window_closed():
	render_all(objects, map)
	libtcod.console_flush()
	for object in objects:
		object.clear()
		
	exit = handle_keys()
	if exit:
		break