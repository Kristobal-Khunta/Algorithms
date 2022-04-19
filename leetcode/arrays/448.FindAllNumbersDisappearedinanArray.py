# Given an array nums of n integers where nums[i] is in the range [1, n],
#  return an array of all the integers in the range [1, n]
#  that do not appear in nums.
# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # O(n) - space
        # O(n) - time
        counts = [0] * (len(nums) + 1)
        for val in nums:
            counts[val] += 1
        return [i for i, val in enumerate(counts) if val == 0 if i != 0]


class Solution2(object):
    # https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/discuss/92955/Python-4-lines-with-short-explanation
    # O(1) - space
    # O(n) - time
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
