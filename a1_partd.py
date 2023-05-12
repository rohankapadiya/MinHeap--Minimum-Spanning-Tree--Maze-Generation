from maze import Maze

def find_path(maze, from_cell, to_cell):
    
	if from_cell == to_cell:
		return [from_cell]
    
	maze.mark_cell(from_cell)

	def cell_is_not_marked(neigh_cell):
		if maze.get_is_marked(neigh_cell) == False:
			return True

	def same_des_neigh_cell(neigh_cell):
		if(neigh_cell == to_cell):
			return [from_cell,neigh_cell]

	find_path_up = maze.get_up(from_cell)
	find_path_down = maze.get_down(from_cell)
	find_path_right = maze.get_right(from_cell)
	find_path_left = maze.get_left(from_cell)

	if cell_is_not_marked(find_path_up):
		if find_path_up != -1:
			same_des_neigh_cell(find_path_up)
			path = find_path(maze,find_path_up,to_cell)
			if path:
				path = [from_cell] + path
				return path

	if cell_is_not_marked(find_path_down):
		if find_path_down != -1:
			same_des_neigh_cell(find_path_down)
			path = find_path(maze,find_path_down,to_cell)
			if path:
				path = [from_cell] + path
				return path

	if cell_is_not_marked(find_path_right):
		if find_path_right != -1:  
			same_des_neigh_cell(find_path_right)
			path = find_path(maze,find_path_right,to_cell)
			if path:
				path = [from_cell] + path
				return path
		
	if cell_is_not_marked(find_path_left):
		if find_path_left != -1:
			same_des_neigh_cell(find_path_left)
			path = find_path(maze,find_path_left,to_cell)
			if path:
				path = [from_cell] + path
				return path
	return []