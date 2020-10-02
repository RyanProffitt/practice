#Specifically for testing the heap tools I made

import heap_tools
	
def test_insert():
	try:
		my_heap = heap_tools.minHeap()
	except Exception as e:
		print(e)
		print("Failed to set up for test_insert. Returning")
		return
	
	try:
		#Test single insertion
		my_heap.insert(5)
		assert(my_heap.size == 1)
		assert(my_heap[0] == 5)
		
		#Check single rotation bubble
		my_heap.insert(3)
		assert(my_heap[0] == 3)
		assert(my_heap[1] == 5)
		
		#check completing the tree
		my_heap.insert(7)
		assert(my_heap[2] == 7)
		
		#check multiple rotation bubble
		my_heap.insert(1)
		assert(my_heap[0] == 1)
		assert(my_heap[1] == 3)
		assert(my_heap[3] == 5)
		
		#check correct size-up
		my_heap.clear()
		for i in range(1024):
			my_heap.insert(1024 - i)
		assert(my_heap.maxsize == 1024)
		my_heap.insert(1)
		assert(my_heap.maxsize == 2048)
		
		print("{0}: PASSED".format(test_insert.__name__))
	except Exception as e:
		print(e)
		print("{0}: FAILED".format(test_insert.__name__))
		
def test_pop():
	try:
		my_heap = heap_tools.minHeap()
		for i in range(3):
			my_heap.insert(i)
		for i in range(3):
			assert(my_heap[i] == i)
		assert(my_heap.size == 3)
	except Exception as e:
		print(e)
		print("Failed setup for test_pop. Returning")
		return
	
	try:
		#Test a single pop
		popped_val = my_heap.pop()
		assert(my_heap.size == 2)
		assert(popped_val == 0)
		assert(my_heap[0] == 1)
		assert(my_heap[1] == 2)
		
		#Test a multiple pop
		my_heap.clear()
		for i in range(7):
			my_heap.insert(i)
		popped_val = my_heap.pop()
		assert(my_heap.size == 6)
		assert(popped_val == 0)
		assert(my_heap[0] == 1)
		assert(my_heap[1] == 3)
		assert(my_heap[2] == 2)
		assert(my_heap[3] == 6)
		assert(my_heap[4] == 4)
		assert(my_heap[5] == 5)
		popped_val = my_heap.pop()
		assert(popped_val == 1)
		assert(my_heap[0] == 2)
		assert(my_heap[1] == 3)
		assert(my_heap[2] == 5)
		assert(my_heap[3] == 6)
		assert(my_heap[4] == 4)
		popped_val = my_heap.pop()
		assert(popped_val == 2)
		assert(my_heap[0] == 3)
		assert(my_heap[1] == 4)
		assert(my_heap[2] == 5)
		assert(my_heap[3] == 6)
		popped_val = my_heap.pop()
		assert(popped_val == 3)
		assert(my_heap[0] == 4)
		assert(my_heap[1] == 6)
		assert(my_heap[2] == 5)
		popped_val = my_heap.pop()
		assert(popped_val == 4)
		assert(my_heap[0] == 5)
		assert(my_heap[1] == 6)
		popped_val = my_heap.pop()
		assert(popped_val == 5)
		assert(my_heap[0] == 6)
		popped_val = my_heap.pop()
		assert(popped_val == 6)
		errors_as_expected = False
		try:
			my_heap.pop()
		except:
			errors_as_expected = True
		assert(errors_as_expected)
		assert(my_heap.size == 0)
		
		print("{0}: PASSED".format(test_pop.__name__))
	except Exception as e:
		print(e)
		print("{0}: FAILED".format(test_pop.__name__))

def main():
	test_insert()
	test_pop()

main()
