# Ryan Proffitt
# 30 May 2021
# Unit tests for the functions found in various/

from fibonacci import fib_recursive
from fibonacci import FibMemoized

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
