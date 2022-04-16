# Два указателя идут навстречу друг другу
# заполняем массив с конца


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
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
