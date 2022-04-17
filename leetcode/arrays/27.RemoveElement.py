class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                if nums[right] != val:
                    nums[left] = nums[right]
                    left += 1
                right -= 1
            else:
                left += 1
        return left

    def removeElementV2(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
