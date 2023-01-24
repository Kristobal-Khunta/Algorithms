class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return (left + 1, right + 1)
            if val > target:
                right -= 1
            if val < target:
                left += 1
