from typing import List


class Solution:
    def __init__(self):
        self.visited = {}

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums and target == 0:
            return 1
        if not nums and target != 0:
            return 0
        prev_nums = nums[:-1]
        prev_pos = target + nums[-1]
        prev_neg = target - nums[-1]
        v_key = (target, len(nums))
        if v_key in self.visited:
            return self.visited[v_key]
        result = self.findTargetSumWays(prev_nums, prev_pos) + self.findTargetSumWays(
            prev_nums, prev_neg
        )
        self.visited[v_key] = result

        return result


class SolutionNeetcode:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)
