import pygame
import math
from constants import *
from utils import *
from algorythms import *
from spot import Statistics

WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption('Algorythm visualiser')

def draw(win, grid, rows, width, stats=None):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	draw_stats(win, stats)
	draw_controls(win, width)
	pygame.display.update()


def main(win, width):
	grid = make_grid(ROWS, width)
	stats = Statistics()

	start = None
	end = None

	run = True 
	started = False 

	while run:
		draw(win, grid, ROWS, width, stats)

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
					stats.reset()

				elif start and end:

					draw_func = lambda: draw(win, grid, ROWS, width, stats)
					if event.key == pygame.K_a:
						run_algorythm(a_star, draw_func, grid, start, end, stats)
					elif event.key == pygame.K_b:
						run_algorythm(bfs, draw_func, grid, start, end, stats)
					elif event.key == pygame.K_d:
						run_algorythm(dijkstra, draw_func, grid, start, end, stats)
					elif event.key == pygame.K_g:
						run_algorythm(greedy_best_first, draw_func, grid, start, end, stats)
		

	pygame.quit()

main(WIN, WIDTH)