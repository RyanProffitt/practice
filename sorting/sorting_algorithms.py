# Ryan Proffitt
# 29 May 2021
# This file is for me to brush up on sorting algorithms.

# This function returns the index at which an item in the list
#   exists such that its value == the parameter val
# If item not found, returns -1
def binary_search(arr, target_val):
    low = 0
    high = len(arr)
    curr_idx = high // 2
    
    search = True
    while search:
        last_idx = curr_idx
        curr_val = arr[curr_idx]

        if curr_val == target_val:
            return curr_idx
        elif target_val < curr_val:
            high = curr_idx
            curr_idx = (curr_idx - low) // 2
        else:
            low = curr_idx
            curr_idx =  (high + curr_idx) // 2
    
        if curr_idx == last_idx:
            search = False
    
    return -1
