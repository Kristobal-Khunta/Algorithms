from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time complexity
        # O(n) space complexity
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        for num, count in counter.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            if not freq[i]:
                continue

            res += freq[i]
            if len(res) == k:
                return res
