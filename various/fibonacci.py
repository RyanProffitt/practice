# Ryan Proffitt
# 30 May 2021
# Fibonnaci Sequence Functions

# A recrusive solution for finding the nth value in the Fibonacci sequence
# Returns: The nth value
# Raises: AssertionError if n < 0
def fib_recursive(n):
    assert n >= 0

    # Base Cases
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)

# A solution for finding the nth value in the Fibonacci sequence, with memoization
class FibMemoized():
    memoized_sequence = {0:0, 1:1} # Base Cases

    def __init__(self):
        pass

    def _fib_helper(self, n):
        if n in FibMemoized.memoized_sequence:
            # If this has been computed before, return the memoized value
            return FibMemoized.memoized_sequence[n]
        
        # Otherwise, compute the missing values
        FibMemoized.memoized_sequence[n] = self._fib_helper(n - 1) + self._fib_helper(n - 2)

        return FibMemoized.memoized_sequence[n]

    # A memoized solution for finding the nth value in the Fibonacci sequence
    #       Makes use of recursion to compute missing values
    # Returns: The nth value
    # Raises: AssertionError if n < 0
    def fib(self, n):
        assert n >= 0

        return self._fib_helper(n)
