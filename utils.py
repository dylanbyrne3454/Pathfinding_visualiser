from spot import Spot 
from constants import *
import pygame

# Manhattan distance heuristic
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2

	return abs(x1 - x2) + abs(y1 - y2)

# Draw shortest path
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

# Create grid of spots
def make_grid(rows, width):
	grid = []
	gap =  width // rows 

	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid 

#Draw grid lines
def draw_grid(win, rows, width):
	gap = width // rows 
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))

	for j in range(rows):
		pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))



def get_clicked_pos(pos, rows, width):
	gap = width // rows 
	y, x = pos

	row = y //gap 
	col = x//gap 

	return row, col 

def run_algorythm(algorythm, draw_func, grid, start, end):
	for row in grid:
		for spot in row:
			spot.update_neighbors(grid)
	algorythm(draw_func, grid, start, end)
