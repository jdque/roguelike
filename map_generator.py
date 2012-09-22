import libtcodpy as libtcod
from map import *

#map generation methods go here

tile_wall = Tile(219, libtcod.Color(255,255,255), libtcod.Color(0,0,0), 1)
tile_floor = Tile(' ', libtcod.Color(0,0,0), libtcod.Color(0,0,0), 0)

def cave(map):

	for y in range(1, map.height-1):
		for x in range(1, map.width-1):
			if libtcod.random_get_int(False, 0, 100) < 45:
				map.set_tile(x, y, tile_wall)

	for i in range(10):

		toggle = [[0
			for y in range(map.height)]
				for x in range(map.width)]	

		for y in range(1, map.height-1):
			for x in range(1, map.width-1):	
				count = 0
				if map.tiles[x][y].type == 1:
					count += 1
				if map.tiles[x-1][y].type == 1:
					count += 1
				if map.tiles[x-1][y+1].type == 1:
					count += 1
				if map.tiles[x][y+1].type == 1:
					count += 1
				if map.tiles[x+1][y+1].type == 1:
					count += 1
				if map.tiles[x+1][y].type == 1:
					count += 1
				if map.tiles[x+1][y-1].type == 1:
					count += 1
				if map.tiles[x][y-1].type == 1:
					count += 1
				if map.tiles[x-1][y-1].type == 1:
					count += 1
					
				if map.tiles[x][y].type == 0 and count >= 5:
					toggle[x][y] = 1
				elif map.tiles[x][y].type == 1 and count >= 4:
					toggle[x][y] = 1

		for a in range(map.height-1):
			for b in range(map.width-1):
				if toggle[a][b] == 1:
					if map.tiles[a-1][b].type == 0 and map.tiles[a+1][b].type == 0 and map.tiles[a][b+1].type == 0 and map.tiles[a][b-1].type == 0:
						map.set_tile(a, b, tile_floor)
					else:
						map.set_tile(a, b, tile_wall)
				else:
					map.set_tile(a, b, tile_floor)