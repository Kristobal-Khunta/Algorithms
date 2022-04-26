# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
    def myPow(self, x, n):
        # x^10 = x^5 * x^5.
        # x^5 = x^2 * x^2 * x.
        if abs(x) < 1e-40:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        lower = self.myPow(x, n // 2)
        if n % 2 == 0:
            return lower * lower
        if n % 2 == 1:
            return lower * lower * x


class Solution:
    # faster than 99%
    # https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/discuss/749109/Python-Recursive-Solution-Faster-than-99
    def myPow(self, x: float, n: int) -> float:
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()

        return float(f) if n >= 0 else 1 / f
