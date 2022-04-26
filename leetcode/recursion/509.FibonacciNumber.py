# The Fibonacci numbers, commonly denoted F(n) form a sequence,
#  called the Fibonacci sequence, such that each number is the
#  sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


class Solution:
    def cache(func):
        hash_map = {}

        def cached(*args, **kwargs):
            if args in hash_map:
                result = hash_map[args]
            else:
                result = func(*args, **kwargs)
                hash_map[args] = result
            return result

        return cached

    @cache
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n - 1) + self.fib(n - 2)


def fib(N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}

    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N - 1) + recur_fib(N - 2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)


def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
