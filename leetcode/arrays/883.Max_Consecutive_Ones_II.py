# Description
# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000.
# Example
# Example 1:
# 	Input:  nums = [1,0,1,1,0]
# 	Output:  4

# 	Explanation:
# 	Flip the first zero will get the the maximum number of consecutive 1s.
# 	After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
# 	Input: nums = [1,0,1,0,1]
# 	Output:  3

# 	Explanation:
# 	Flip each zero will get the the maximum number of consecutive 1s.
# 	After flipping, the maximum number of consecutive 1s is 3.
# https://www.lintcode.com/problem/883/solution/29011


class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def find_max_consecutive_ones(self, nums):
        # write your code here
        sum_with_flip = 0
        sum_wo_flip = 0
        max_sum = 0
        for val in nums:
            if val == 1:
                sum_with_flip += 1
                sum_wo_flip += 1
            if val == 0:
                sum_with_flip = sum_wo_flip + 1
                sum_wo_flip = 0
            max_sum = max(max_sum, sum_with_flip)
        return max_sum


class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        can_still_flip, no_more_flips, max_ones = 0, 0, 0

        for num in nums:

            if num == 1:
                can_still_flip += 1
                no_more_flips += 1
            else:
                can_still_flip += 1
                no_more_flips, can_still_flip = can_still_flip, 0

            max_ones = max(max_ones, can_still_flip, no_more_flips)

        return max_ones
