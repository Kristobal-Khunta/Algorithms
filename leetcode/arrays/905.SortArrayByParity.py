# Given an integer array nums, move all the even integers
#  at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        техника  - 2 указателя навстречу друг другу
        инвариант 1 - слева от левого -только четные
        # справа от правого -только нечетные
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            left_odd = nums[left] % 2
            right_odd = nums[right] % 2
            if left_odd and not right_odd:
                nums[right], nums[left] = nums[left], nums[right]
            if not left_odd:
                left += 1
            if right_odd:
                right -= 1
        return nums


class Solution(object):
    #https://leetcode.com/problems/sort-array-by-parity/solution/
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1

        return A
