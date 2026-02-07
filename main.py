import pygame
import math
from constants import *
from utils import *
from algorythms import *


WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption('Algorythm visualiser')

def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def main(win, width):
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True 
	started = False 

	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start:
					start = spot
					start.make_start()


				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()

				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

				elif start and end:

					if event.key == pygame.K_a:
						run_algorythm(a_star, lambda: draw(win, grid, ROWS, width), grid, start, end)
					elif event.key == pygame.K_b:
						run_algorythm(bfs, lambda: draw(win, grid, ROWS, width), grid, start, end)
					elif event.key == pygame.K_d:
						run_algorythm(dijkstra, lambda: draw(win, grid, ROWS, width), grid, start, end)
					elif event.key == pygame.K_g:
						run_algorythm(greedy_best_first, lambda: draw(win, grid, ROWS, width), grid, start, end)
		

	pygame.quit()

main(WIN, WIDTH)