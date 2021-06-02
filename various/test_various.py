# Ryan Proffitt
# 30 May 2021
# Unit tests for the functions found in various/

from fibonacci import fib_recursive
from fibonacci import FibMemoized

from satellite_pass_tools import get_max_necessary_bandwidth

_fib_val_dict = {
    0:0,
    1:1,
    2:1,
    3:2,
    4:3,
    5:5,
    8:21,
    9:34,
    10:55,
    30:832040,
    31:1346269,
    32:2178309,
    33:3524578,
    34:5702887,
    35:9227465
}

def _assert_fib_val_using_dict(n, val):
    assert val == _fib_val_dict[n], "Warning to tester, n is not in the test dictionary!"

def test_fib_recursive():
    _assert_fib_val_using_dict(0, fib_recursive(0))
    _assert_fib_val_using_dict(1, fib_recursive(1))
    _assert_fib_val_using_dict(2, fib_recursive(2))
    _assert_fib_val_using_dict(3, fib_recursive(3))
    _assert_fib_val_using_dict(4, fib_recursive(4))
    _assert_fib_val_using_dict(5, fib_recursive(5))

    _assert_fib_val_using_dict(8, fib_recursive(8))
    _assert_fib_val_using_dict(9, fib_recursive(9))
    _assert_fib_val_using_dict(10, fib_recursive(10))

    # Only testing to n = 30 because of runtime issues for n > 30
    _assert_fib_val_using_dict(30, fib_recursive(30))

def test_fib_memoized():
    my_fib = FibMemoized()
    _assert_fib_val_using_dict(30, my_fib.fib(30))
    _assert_fib_val_using_dict(31, my_fib.fib(31))
    _assert_fib_val_using_dict(32, my_fib.fib(32))

    # Should be almost instant due to memoization
    # (results may vary depending on whatever processor is doing right now)
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))
    _assert_fib_val_using_dict(32, my_fib.fib(32))

    _assert_fib_val_using_dict(33, my_fib.fib(33))
    _assert_fib_val_using_dict(34, my_fib.fib(34))
    _assert_fib_val_using_dict(35, my_fib.fib(35))

    try:
        _assert_fib_val_using_dict(0, my_fib.fib(-1))
    except AssertionError:
        pass # Failed successfully

    try:
        _assert_fib_val_using_dict(1, my_fib.fib(5))
    except AssertionError:
        pass # Failed successfully

    try:
        _assert_fib_val_using_dict(34, my_fib.fib(35))
    except AssertionError:
        pass # Failed successfully

def test_get_max_necessary_bandwidth():
    sample_pass_schedule = [
        [0,2,4,10],
        [1,3,5,20],
        [2,4,5,30],
        [1,6,10,40],
        [2,12,20,50],
        [1,14,16,100],
        [0,17,19,150]
    ]

    assert get_max_necessary_bandwidth(sample_pass_schedule) == 200

    sample_pass_schedule = [
        [0,1619946610000,1619947090000,14],
        [1,1619946730000,1619947210000,28],
        [2,1619946010000,1619946310000,14],
        [1,1619947330000,1619947680000,7],
        [2,1619947530000,1619947830000,14],
        [1,1619948270000,1619948810000,7],
        [0,1619948410000,1619948530000,12]
    ]

    assert get_max_necessary_bandwidth(sample_pass_schedule) == 42

    sample_pass_schedule = [
        [0,1619946610000,1619947090000,14],
        [1,1619947090000,1619947190000,28],
        [2,1619947090000,1619947190000,28],
    ]

    assert get_max_necessary_bandwidth(sample_pass_schedule) == 56

    sample_pass_schedule = []

    assert get_max_necessary_bandwidth(sample_pass_schedule) == 0

    sample_pass_schedule = [
        [0,1619946610000,1619947090000,14]
    ]

    assert get_max_necessary_bandwidth(sample_pass_schedule) == 14

test_get_max_necessary_bandwidth()