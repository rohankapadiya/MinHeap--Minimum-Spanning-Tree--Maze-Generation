from a1_partb import SetList

class DisjointSet:
	def __init__(self):
		self.parent = {}
		self.step_size = {}    
		self.num_of_sets = 0
		self.num_of_elements = 0

	def make_set(self, element):
		if element in self.parent :
			return False
		else:
			n_node = SetList.Node(element)
			self.parent[element] = n_node.get_data()
			self.step_size[element] = 1
			self.num_of_sets = self.num_of_sets + 1
			self.num_of_elements = self.num_of_elements + 1  
			return True

	def get_set_size(self,element):
		if element in self.parent:
			return self.step_size[self.find_set(element)]
		else:
			return 0

	def find_set(self, element):
		if element not in self.parent:
			return None

		if (self.parent[element] != element): 
			self.parent[element] = self.find_set(self.parent[element])
		
		return self.parent[element]

	def union_set(self, element1, element2):
		if element1 not in self.parent:
			return False

		if element2 not in self.parent:
			return False

		if self.find_set(element1) == self.find_set(element2):
			return False

		if self.get_set_size(element1) < self.get_set_size(element2):
			count = 0
			self.num_of_sets = self.num_of_sets - 1
			self.parent[self.find_set(element1)] = self.parent[self.find_set(element2)]
			self.step_size[self.find_set(element2)] = self.step_size[self.find_set(element2)] + self.step_size[self.find_set(element1)]
			
			for element in self.parent: 
				if self.parent[element] == self.parent[self.find_set(element2)]:
					count = count + 1
     
			if (self.step_size[self.find_set(element2)] > count):
				self.step_size[self.find_set(element2)] = self.step_size[self.find_set(element2)] - 1

		else:
			count = 0
			self.num_of_sets = self.num_of_sets - 1
			self.parent[self.find_set(element2)] = self.parent[self.find_set(element1)]
			self.step_size[self.find_set(element1)] = self.step_size[self.find_set(element1)] + self.step_size[self.find_set(element2)]
			
			for element in self.parent:
				if self.parent[element] == self.parent[self.find_set(element1)]:
						count = count + 1
      
			if (self.step_size[self.find_set(element1)] > count):
				self.step_size[self.find_set(element1)] = self.step_size[self.find_set(element1)] - 1
    
		return True

	def get_num_sets(self):
		return self.num_of_sets

	def __len__(self):
		return self.num_of_elements