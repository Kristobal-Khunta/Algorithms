from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        slower = 0
        faster = 1
        while faster < len(nums):
            if nums[faster] != nums[slower]:
                slower += 1
                nums[slower] = nums[faster]
            faster += 1
        return slower + 1

    def v2(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1
        return x
