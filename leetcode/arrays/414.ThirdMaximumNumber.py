#
# Given an integer array nums, return the third distinct
# maximum number in this array. If the third maximum does not exist,
#  return the maximum number.
from typing import List
import math


class Solution:
    # my solution

    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        max_arr = [-math.inf] * 3  # sorted([nums[0],nums[1],nums[2]])
        for i in range(0, len(nums)):
            val = nums[i]
            if val > max_arr[0] and val not in max_arr:
                if val > max_arr[2]:
                    max_arr[0], max_arr[1], max_arr[2] = max_arr[1], max_arr[2], val
                elif val > max_arr[1]:
                    max_arr[0], max_arr[1] = max_arr[1], val
                else:
                    max_arr[0] = val
        if min(max_arr) == -math.inf:
            return max(max_arr)
        return max_arr[0]


# from duscuss
class Solution(object):
    def thirdMax(self, nums):
        v = [float("-inf"), float("-inf"), float("-inf")]
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
        return max(nums) if float("-inf") in v else v[2]
