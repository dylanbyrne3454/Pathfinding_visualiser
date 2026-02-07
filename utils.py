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

def draw_stats(win, stats):
	if not stats or stats.algorithm_name == "":
		return

	pygame.font.init()
	font = pygame.font.SysFont('Arial', 20)

	#Statistics shown
	texts = [
		f"Algorithm: {stats.algorithm_name}",
		f"Nodes Explored: {stats.nodes_explored}",
		f"Path Length: {stats.path_length}",
		f"Time: {stats.time_taken * 1000:.2f} ms"
	]
	
	box_height = 30* len(texts) + 20
	pygame.draw.rect(win, (50, 50, 50), (10, 10, 300, box_height))

	y_offset = 20
	for text in texts:
		text_surface = font.render(text, True, (255, 255, 255))
		win.blit(text_surface, (20, y_offset))
		y_offset += 30

def get_clicked_pos(pos, rows, width):
	gap = width // rows 
	y, x = pos

	row = y //gap 
	col = x//gap 

	return row, col 

def run_algorythm(algorythm, draw_func, grid, start, end, stats=None):
	for row in grid:
		for spot in row:
			spot.update_neighbors(grid)
	algorythm(draw_func, grid, start, end, stats)
