# Given an integer array nums, move all 0's to the end of it
#  while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1-й инвариант все элементы до медленного указателя !=0
        2-й инвариант - между медленным и быстрым указателем все значения = 0

        """
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
