from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time: O(N)
        Space: O(N)
        optimal space: O(1)
        reverse order, without stack
         https://leetcode.com/problems/daily-temperatures/solutions/1516538/official-solution/
        """
        
        ans = [0] * len(temperatures)
        stack = []  # (idx,temp)
        for i, t in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and t > stack[-1][1]:
                idx_top, t_top = stack.pop()
                days_diff = i - idx_top
                ans[idx_top] = days_diff
            stack.append((i, t))
        return ans
