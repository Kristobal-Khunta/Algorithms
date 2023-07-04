class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float("-inf")
        cur_max = 0

        for val in nums:
            cur_max += val

            # Update max_subarray with the max of max_subarray and cur_max
            global_max = max(global_max, cur_max)

            # Reset cur_max to 0 if the current subarray sum is non-positive
            if cur_max < 0:
                cur_max = 0

        return global_max
