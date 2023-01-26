from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        Time complexity: O(n^2)
        Space complexity: O(n) (sorting algo)
        """
        nums.sort()
        results = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[idx] + nums[right]
                if threeSum > 0:
                    right -= 1
                if threeSum < 0:
                    left += 1
                if threeSum == 0:
                    results.append([nums[left], nums[right], nums[idx]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return results


class SolutionOfficial:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
