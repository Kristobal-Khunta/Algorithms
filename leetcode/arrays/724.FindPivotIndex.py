from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        sum_right = sum(nums)
        sum_left = 0

        for i, val in enumerate(nums):
            sum_right -= val
            if sum_left == sum_right:
                return i
            sum_left += val
        return -1


class SolutionOfficial(object):
    """
    Time Complexity: O(N), where N is the length of nums.
    Space Complexity: O(1), the space used by leftsum and S
    """
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1