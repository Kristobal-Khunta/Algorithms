from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val > target:
                right = mid
            else:
                left = mid + 1
        return res


class SolutionV2:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return res
