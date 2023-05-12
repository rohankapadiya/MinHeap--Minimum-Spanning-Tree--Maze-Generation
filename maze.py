#
#   Author: Catherine Leung
#   The Maze class represents a maze and provides functions that you can use
#   to find a path through the maze.  The code is not to be altered.  During
#   testing, this file be pulled from the original source.  any code you write
#   cannot be in this file.
#   the_maze object passed to find_path is an instance of Maze 
#   Tested using Python 3.10
#
import json

class Maze:
	def __init__(self,filename):
		file = open(filename, "r")
		lines = file.readlines()
		dimensions = json.loads(lines[0])
		themaze = json.loads(lines[1])
		file.close()
		
		self.num_rows = dimensions['maxRow']
		self.num_cols = dimensions['maxCol']
		self.num_cells = self.num_rows * self.num_cols
		self.cells = [False for i in range(self.num_cells)]
		self.walls = [[False for j in range(self.num_cells)] for i in range(self.num_cells)]
		for the_cells in themaze["walls"]:
			self.walls[the_cells[0]][the_cells[1]] = True
			self.walls[the_cells[1]][the_cells[0]] = True


	# returns total number of rows in the maze
	def get_num_rows(self):
		return self.num_rows

	# returns total number of columns in the maze
	def get_num_cols(self):
		return self.num_cols

	# returns the cell_number given row and col
	def get_cell(self, row, col):
		return row * self.num_cols + col

	# returns the row given cell_number
	def get_row(self, cell_number):
		return cell_number//self.num_cols

	# returns the col given cell_number
	def get_col(self, cell_number):
		return cell_number % self.num_cols

	# returns the cell_number of the cell to the left of the cell_number
	# if there is no cell on the left or there is a wall between current cell 
	# and left cell, function returns -1
	def get_left(self, cell_number):
		col = self.get_col(cell_number)
		row = self.get_row(cell_number)
		if col == 0:
			return -1
		else:
			left_cell = self.get_cell(row,col-1)
			if not self.walls[left_cell][cell_number]:
				return left_cell
			return -1


	# returns the cell_number of the cell to the right of the cell_number
	# if there is no cell on the right or there is a wall between current cell 
	# and right cell, function returns -1
	def get_right(self, cell_number):
		col = self.get_col(cell_number)
		row = self.get_row(cell_number)
		if col == self.num_cols-1:
			return -1
		else:
			right_cell = self.get_cell(row,col+1)
			if not self.walls[right_cell][cell_number]:
				return right_cell
			return -1

	# returns the cell_number of the cell to the up of the cell_number
	# if there is no cell on the up or there is a wall between current cell 
	# and up cell, function returns -1
	def get_up(self, cell_number):
		col = self.get_col(cell_number)
		row = self.get_row(cell_number)
		if row == 0:
			return -1
		else:
			up_cell = self.get_cell(row-1,col)
			if not self.walls[up_cell][cell_number]:
				return up_cell
			return -1


	# returns the cell_number of the cell to the down of the cell_number
	# if there is no cell on the down or there is a wall between current cell 
	# and down cell, function returns -1
	def get_down(self, cell_number):
		col = self.get_col(cell_number)
		row = self.get_row(cell_number)
		if row == self.num_rows-1:
			return -1
		else:
			down_cell = self.get_cell(row+1,col)
			if not self.walls[down_cell][cell_number]:
				return down_cell
			return -1

	# marks the cell with cell_number, this will allow you to leave a mark on
	# the cells that are part of your path (or being considered to be on your path)
	def mark_cell(self, cell_number):
		self.cells[cell_number]=True

	# ummarks the cell 
	def unmark_cell(self, cell_number):
		self.cells[cell_number]=False

	# returns true of cell_number is marked, false otherwise
	def get_is_marked(self,cell_number):
		return self.cells[cell_number]


def print_pathfile(filename, result, row, col):

	the_file = open(filename,"w")
	the_file.write(f'{{"rows": {row}, "cols": {col},')
	the_file.write(f' "pathLength": {len(result)},')
	the_file.write(f'"path":{result}')
	the_file.write("}")
	the_file.close()



