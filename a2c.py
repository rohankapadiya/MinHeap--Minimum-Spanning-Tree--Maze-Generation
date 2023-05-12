# if you wish to use your sorted table_list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.value = value
		def value_setter(self,value):
			self.value = value
		def key_retriever(self):
			return self.key
		def value_retriever(self):
			return self.value

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.cap = cap
		self.length = 0
		self.table_list = [None for i in range(self.cap)]
		self.checking = ["empty" for i in range(self.cap)]
		

	def insert(self,key, value):
		add_hash = hash(key) % self.cap

		while self.checking[add_hash] != "empty":
      
			if self.table_list[add_hash].key_retriever() == key:
				return False

			add_hash = (add_hash + 1) % self.cap

		lf = (self.length+1) / self.cap
  
		if lf > 0.7:
      
			temp_list = [None for i in range(self.cap*2)]
   
			temp_status = ["empty" for i in range(self.cap*2)]
   

			for e in self.table_list:
				if e is not None:
        
					add_hash = hash(e.key_retriever()) % (self.cap*2)
     
					while temp_status[add_hash] != "empty":
						add_hash = (add_hash+1) % (self.cap * 2)
      
					temp_list[add_hash] = e
					temp_status[add_hash] = "used"
			
			self.table_list = temp_list
			self.checking = temp_status
			self.cap = self.cap*2
		
		add_hash = hash(key) % self.cap
  
		while self.checking[add_hash] != "empty" and self.checking[add_hash] != "deleted":
			add_hash = (add_hash+1) % self.cap
		
		self.table_list[add_hash] = self.Record(key,value)
		self.checking[add_hash] = "used"
		self.length+= 1
  
		return True


	def modify(self, key, value):
     
		add_hash = hash(key) % self.cap
  
		while self.checking[add_hash] != "empty":
      
			if self.table_list[add_hash].key_retriever() == key:
				self.table_list[add_hash].value_setter(value)
				return True

			add_hash = (add_hash + 1) % self.cap
   
		return False
				

	def remove(self, key):
     
		add_hash = hash(key) % self.cap
  
		while self.checking[add_hash] != "empty":
      
			if self.checking[add_hash] != "deleted" and self.table_list[add_hash].key_retriever() == key:
				self.table_list[add_hash] = None
				self.checking[add_hash] = "deleted"
				self.length -= 1
				return True

			add_hash = (add_hash + 1) % self.cap
   
		return False


	def search(self, key):
     
		add_hash = hash(key) % self.cap
  
		while self.checking[add_hash] != "empty":
      
			if self.checking[add_hash] != "deleted" and self.table_list[add_hash].key_retriever() == key:
				return self.table_list[add_hash].value_retriever()

			add_hash = (add_hash+1) % self.cap
   
		return None

	def capacity(self):
		return self.cap

	def __len__(self):
		return self.length


class LinearProbingNoTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.value = value
		def value_setter(self,val):
					self.value = val
		def key_retriever(self):
			return self.key
		def value_retriever(self):
			return self.value
	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)
	
	def __init__(self, cap=32):
		self.cap = cap
		self.length = 0
		self.table_list = [None for i in range(self.cap)]
		
	def insert(self,key, value):
		add_hash = hash(key) % self.cap

		while self.table_list[add_hash] is not None:
      
			if self.table_list[add_hash].key_retriever() == key:
				return False

			add_hash = (add_hash + 1) % self.cap

		lf = (self.length+1) / self.cap
  
		if lf > 0.7:
			temp_list = [None for i in range(self.cap*2)]

			for e in self.table_list:
				if e is not None:
					add_hash = hash(e.key_retriever()) % (self.cap*2)
     
					while temp_list[add_hash] is not None:
						add_hash = (add_hash+1) % (self.cap * 2)
      
					temp_list[add_hash] = e
			
			self.table_list = temp_list
			self.cap = self.cap*2
		
		add_hash = hash(key) % self.cap
  
		while self.table_list[add_hash] is not None:
			add_hash = (add_hash+1) % self.cap
		
		self.table_list[add_hash] = self.Record(key,value)
		self.length+= 1
  
		return True

	def modify(self, key, value):
		add_hash = hash(key) % self.cap
  
		while self.table_list[add_hash] is not None:
      
			if self.table_list[add_hash].key_retriever() == key:
				self.table_list[add_hash].value_setter(value)
				return True

			add_hash = (add_hash + 1) % self.cap
   
		return False

	def remove(self, key):
		add_hash = hash(key) % self.cap
		flag = False
		emptySpot = None
  
		while not flag and self.table_list[add_hash] is not None:
      
			if self.table_list[add_hash].key_retriever() == key:
				self.table_list[add_hash] = None
				self.length -= 1
				emptySpot = add_hash
				flag = True
    
			add_hash = (add_hash+1) % self.cap

		while flag and self.table_list[add_hash] is not None:
      
			hashIdx = hash(self.table_list[add_hash].key_retriever()) % self.cap
   
			while hashIdx != add_hash:
       
				if hashIdx == emptySpot:
					self.table_list[hashIdx] = self.table_list[add_hash]
					self.table_list[add_hash] = None
     
				if hashIdx == None or hashIdx == add_hash:
					break
 
				hashIdx = (hashIdx+1) % self.cap
    
			add_hash = (add_hash+1) % self.cap

		return flag

	def search(self, key):
     
		add_hash = hash(key) % self.cap
  
		while self.table_list[add_hash] is not None:
      
			if self.table_list[add_hash].key_retriever() == key:
				return self.table_list[add_hash].value_retriever()

			add_hash = (add_hash + 1) % self.cap
   
		return None



	def capacity(self):
		return self.cap

	def __len__(self):
		return self.length


