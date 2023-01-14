"""
It eventually gets to 111.
It eventually gets stuck in a cycle.
It keeps going higher and higher, up towards infinity.

For a number with 3 digits, it's impossible for it to ever go larger than 243(9^2+9^2+9^2). This means it will have to either get stuck in a cycle below 243 or go down to 111. Numbers with 444 or more digits will always lose a digit at each step until they are down to 3 digits. So we know that at worst, the algorithm might cycle around all the numbers under 243 and then go back to one it's already been to (a cycle) or go to 1. But it won't go on indefinitely, allowing us to rule out the 3rd option.

Even though you don't need to handle the 3rd case in the code, you still need to understand why it can never happen, so that you can justify why you didn't handle it.

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(x) for x in str(n)]
        seen = set()
        sum_sq = -1
        while sum_sq != 1:
            sum_sq = sum([x**2 for x in digits])
            if sum_sq in seen:
                return False
            seen.add(sum_sq)
            digits = [int(x) for x in str(sum_sq)]
        return True


class SolutionOfficial:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
