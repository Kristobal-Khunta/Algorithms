# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.


class Solution:
    def findNumDigits(self, num: int) -> int:
        count: int = 0
        while num >= 10:
            count += 1
            num = num // 10
        count += 1
        return count

    def findNumbers(self, nums: list[int]) -> int:
        max_counter = 0
        for num in nums:
            num_digits = self.findNumDigits(num)
            odd_num = num_digits % 2
            if not odd_num:
                max_counter += 1
        return max_counter
