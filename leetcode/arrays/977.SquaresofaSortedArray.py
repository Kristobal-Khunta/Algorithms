# Два указателя идут навстречу друг другу
# заполняем массив с конца
import collections 
from typing import List


class Solution:
    # mine 
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if nums[0] >= 0:
            return [num**2 for num in nums]
        r_pointer = len(nums) - 1
        l_pointer = 0
        right = nums[r_pointer] ** 2
        left = nums[l_pointer] ** 2
        result = [None] * len(nums)
        rev_idx = len(nums) - 1
        while rev_idx >= 0:
            if left > right:  # нельзя >= не прозодит тест [-4,-1]
                result[rev_idx] = left
                l_pointer += 1
                left = nums[l_pointer] ** 2
            else:
                result[rev_idx] = right
                r_pointer -= 1
                right = nums[r_pointer] ** 2
            rev_idx -= 1
        return result


class Solution:
    # similar but beauty
    def sortedSquares(self, A: List[int]) -> List[int]:
        return_array = [0] * len(A)
        write_pointer = len(A) - 1
        left_read_pointer = 0
        right_read_pointer = len(A) - 1
        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        while write_pointer >= 0:
            if left_square > right_square:
                return_array[write_pointer] = left_square
                left_read_pointer += 1
                left_square = A[left_read_pointer] ** 2
            else:
                return_array[write_pointer] = right_square
                right_read_pointer -= 1
                right_square = A[right_read_pointer] ** 2
            write_pointer -= 1
        return return_array

def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)