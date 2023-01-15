from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        hashmap = {}  # {val:index}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[n] = idx
        return None
