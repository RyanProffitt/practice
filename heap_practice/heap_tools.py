#This is just for me to get some practice implementing heap tools.

#This Tree is a minimum heap
#	The root of this tree will be the smallest value in the tree
class minHeap:
	def __init__(self):
		self.maxsize = 1024
		self.heap = [None] * self.maxsize
		self.size = 0
		
	#Gets the parent position of the node at index pos
	#Accepts position
	#Returns parent position
	def get_parent_pos(self, pos):
		if pos % 2 == 0:
			return pos / 2 - 1
		else:
			return pos // 2
		
	#Gets the left child position of the node at index pos
	#Accepts position
	#Returns left child position
	def get_left_child_pos(self, pos):
		return pos * 2 + 1
		
	#Gets the right child position of the node at index pos
	#Accepts position
	#Returns right child position
	def get_right_child_pos(self, pos):
		return pos * 2 + 2
		
	#Returns the value of the top position
	def peek(self):
		if self.size > 0:
			return self.heap[0]
		else:
			raise IndexError
	
	#Swaps the values at two given positions posA and posB
	def _swap(self, posA, posB):
		self.heap[posA], self.heap[posB] = self.heap[posB], self.heap[posA]
		
	#Bubbles a value up the heap if it is smaller in value than its parent
	#Accepts a given position
	def _bubbleUp(self, curr_pos):
		while self.heap[curr_pos] < self.heap[self.get_parent_pos(curr_pos)]:
			self._swap(self.get_parent_pos(curr_pos), curr_pos)
			curr_pos = self.get_parent_pos(curr_pos)
			
	#Bubbles a value down the heap if it is smaller in value than its smallest child
	#Accepts a given position
	def _bubbleDown(self, curr_pos):
		not_leaf = True
		while not_leaf:
			left_child_pos = self.get_left_child_pos(curr_pos)
			right_child_pos = self.get_right_child_pos(curr_pos)
			
			#get the lowest value child
			minimum_child_pos = -1
			if self.heap[left_child_pos] and self.heap[right_child_pos]:
				if self.heap[left_child_pos] <= self.heap[right_child_pos]:
					minimum_child_pos = left_child_pos
				else:
					minimum_child_pos = right_child_pos
			elif self.heap[left_child_pos] and not self.heap[right_child_pos]:
				minimum_child_pos = left_child_pos
			elif not self.heap[left_child_pos] and self.heap[right_child_pos]:
				minimum_child_pos = right_child_pos
			else:
				not_leaf = False
				continue
				
			#see if the current value is larger than the lowest value child
			#if it is, then bubble down
			#otherwise, the current value is in the correct pos
			if self.heap[curr_pos] > self.heap[minimum_child_pos]:
				#print(str(self.heap[curr_pos]), " > ", str(self.heap[minimum_child_pos]))
				self._swap(curr_pos, minimum_child_pos)
			else:
				not_leaf = False
				continue
			
			curr_pos = minimum_child_pos
		
	#Inserts a value into the heap
	#Accepts a value
	def insert(self, val):
		#print("Inserting val", str(val))
		if self.size + 1 > self.maxsize:
			self.maxsize *= 2
			self.heap.extend([None] * self.maxsize)
		
		self.heap[self.size] = val
		
		#print("heap[{0}] == {1}".format(self.size, val))
		
		self._bubbleUp(self.size)
		
		self.size += 1
		
	#Gets and removes the root position value
	#Returns the value
	#Exceptions
	#	Uses peek() which returns an IndexError exception if the heap is empty
	def pop(self):
		return_val = self.peek()
		self.heap[0] = self.heap[self.size - 1]
		self.heap[self.size - 1] = None
		self.size -= 1
		self._bubbleDown(0)
		return return_val
		
	def __str__(self):
		return str(self.heap[:self.size])
		
	def __getitem__(self, pos):
		return self.heap[pos]
	
	#reduces the size of the heap to its base size and removes all values
	def clear(self):
		self.maxsize = 1024
		self.heap = [None] * self.maxsize
		self.size = 0
