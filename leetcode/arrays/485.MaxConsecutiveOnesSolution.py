# Given a binary array nums, return the maximum number of consecutive 1's in the array.


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter: int = 0
        max_counter: int = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                counter = 0
            max_counter = max(max_counter, counter)
        return max_counter
