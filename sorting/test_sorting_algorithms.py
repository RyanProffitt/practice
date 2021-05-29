# Ryan Proffitt
# 29 May 2021
# This file contains code to test the sorting_algorithms.

from random import randint

import sorting_algorithms

def test_binary_search():
    print("TESTING: binary_search()")

    # Test random arrays a given number of times
    for i in range(100):
        # Create a list of random integers
        list_len = 1024
        my_list = [randint(0, list_len) for i in range(list_len)]

        # Create an arbitrary value to search for and insert into list
        arb_val = randint(0, list_len)
        my_list[randint(0, list_len)] = arb_val

        # Sort the list
        my_list.sort()

        # Search the list for the arbitrary integer
        resulting_idx = sorting_algorithms.binary_search(my_list, arb_val)

        assert my_list[resulting_idx] == arb_val

    # Test specific values at known positions
    my_list = [0, 1, 1, 2, 4, 4, 4, 4, 8, 9, 10, 15, 16, 19, 20]
    assert sorting_algorithms.binary_search(my_list, 0) == 0
    assert sorting_algorithms.binary_search(my_list, 20) == 14
    assert sorting_algorithms.binary_search(my_list, 4) == 7
    assert sorting_algorithms.binary_search(my_list, 8) == 8

    print("PASSED: binary_search()")

# test_binary_search()
