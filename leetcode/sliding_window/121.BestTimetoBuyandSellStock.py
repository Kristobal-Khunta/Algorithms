from typing import List


class Solution2pointer:
    def maxProfit(self, prices: List[int]) -> int:
        # time: O(n), memory: O(1)
        l = 0
        r = 1
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower = prices[0]
        res = 0
        for p in prices:
            if p < lower:
                lower = p
            res = max(res, p - lower)
        return res
