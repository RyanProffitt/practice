#This module tests Linked Lists code I created
import linked_list_tools

def main():
	firstNode = linked_list_tools.LLNode(7)
	firstList = linked_list_tools.LList()
	print(firstList)
	
	#try to add a non-LLNode object
	try:
		firstList.add(11)
	except Exception as e:
		print(e)
		print("Successfully failed to add a non-Node object")
	
	llist_iter = iter(firstList)
	curr = next(llist_iter)
	while curr:
		print(curr)
	
	secondNode = LLNode(8)
	thirdNode = LLNode(9)
	firstList.add_node(secondNode)
	firstList.add_node(thirdNode)
	
	llist_iter = iter(firstList)
	curr = next(llist_iter)
	while curr:
		print(curr)
		curr = next(llist_iter)
	
if __name__ == "__main__":
	main()
