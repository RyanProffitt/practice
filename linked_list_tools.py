#I understand that linked lists are not really a "concept" of Python.
# I'm going to implement them in Python anyways just to play around
# with some practice problems

#In this file, you will find linked list tools, like nodes, the linked list
# class, and just a few basic functions

class LLNode():
	def __init__(self, val):
		self.val = val
		self.next = None
		
	def __repr__(self):
		return "LLNode()"
	
	def __str__(self):
		return "LLNode Val ({0}), Next ({1})".format(self.val, self.next)

#A Linked List class
# Lists can be created empty
class LList():
	def __init__(self):
		self.head = None
		self.len = 0
		
	def __repr__(self):
		return "LList()"
		
	def __str__(self):
		return "LList Head ({0})".format(self.head)
		
	#Sets up an iterator starting at the first Node in the list
	# Note that returning None is expected behavior if list is empty
	def __iter__(self):
		self.curr = self.head
		return self
		
	#Gets the next Node in this linked list
	# Returns None if there is no next node (expected behavior of Node class)
	def __next__(self):
		ret_node = self.curr
		self.curr = self.curr.next
		return self.curr_next
			
	#Adds a node to the end of the list
	# This will set the given node's node.next to None
	def add_node(self, node):
		if not isinstance(node, LLNode):
			raise ValueError("add_node() expected an instance of LLNode, but got {0} instead".format(type(node)))
		#handle first node
		if self.len == 0:
			self.head = node
			self.len = 1
		
		#setup to handle a list with N > 0 nodes
		llist_iter = iter(self)
		curr_node = self.head
		
		#find the end of the list
		while curr_node.next:
			curr_node = next(curr_node)
		
		self.len = self.len + 1
		curr_node.next = node
