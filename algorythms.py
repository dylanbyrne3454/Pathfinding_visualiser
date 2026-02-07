from queue import PriorityQueue
from utils import h, reconstruct_path
import pygame
import time

def a_star(draw, grid, start, end, stats=None):
	start_time = time.time()

	if stats:
		stats.reset()
		stats.algorithm_name = "A*"  # ✅ Fixed

	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float('inf') for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float('inf') for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if stats:
			stats.nodes_explored += 1  # ✅ Fixed (added 's')

		if current == end:
			if stats:
				path_len = 0 
				temp = end  
				while temp in came_from:
					path_len += 1
					temp = came_from[temp]
				stats.path_length = path_len  # ✅ Fixed
				stats.time_taken = time.time() - start_time  # ✅ Fixed

			reconstruct_path(came_from, end, draw) 
			end.make_end()
			return True  

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	if stats:
		stats.time_taken = time.time() - start_time

	return False
	
def dijkstra(draw, grid, start, end, stats=None):
	start_time = time.time()
	
	if stats:
		stats.reset()
		stats.algorithm_name = "Dijkstra"

	count = 0
	open_set = PriorityQueue()
	open_set.put((0,count, start))
	came_from = {}


	g_score = {spot: float('inf') for row in grid for spot in row}
	g_score[start] = 0
	
	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if stats:
			stats.nodes_explored += 1

		if current == end:
			if stats:
				path_len = 0
				temp = end
				while temp in came_from:
					path_len += 1
					temp = came_from[temp]
				stats.path_length = path_len
				stats.time_taken = time.time() - start_time
			
			reconstruct_path(came_from, end, draw) 
			end.make_end()
			return True  

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score

				if neighbor not in open_set_hash:
					count += 1
					open_set.put((g_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	if stats:
		stats.time_taken = time.time() - start_time

	return False

def greedy_best_first(draw, grid, start, end, stats=None):
	start_time = time.time()
	
	if stats:
		stats.reset()
		stats.algorithm_name = "Greedy"

	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	open_set_hash = {start}
	visited = set()
	
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		current = open_set.get()[2]
		open_set_hash.remove(current)
		
		if current in visited:
			continue
		visited.add(current)

		if stats:
			stats.nodes_explored += 1

		if current == end:
			if stats:
				path_len = 0
				temp = end
				while temp in came_from:
					path_len += 1
					temp = came_from[temp]
				stats.path_length = path_len
				stats.time_taken = time.time() - start_time
			
			reconstruct_path(came_from, end, draw) 
			end.make_end()
			return True  
		
		for neighbor in current.neighbors:
			if neighbor not in open_set_hash and neighbor not in visited:
				came_from[neighbor] = current
				count += 1
				h_score = h(neighbor.get_pos(), end.get_pos())
				open_set.put((h_score, count, neighbor)) 
				open_set_hash.add(neighbor)
				neighbor.make_open()
		
		draw()
		if current != start:
			current.make_closed()
	if stats:
		stats.time_taken = time.time() - start_time

	return False
