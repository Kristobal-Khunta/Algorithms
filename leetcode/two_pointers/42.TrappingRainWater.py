class Solution:
    """
    time complexity: O(n)
    space complexity: O(n)
    """"
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left = [0] * (len(height))
        max_right = [0] * (len(height))
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, len(max_left)):
            max_left[i] = max(max_left[i - 1], height[i])
        for j in range(len(max_right) - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], height[j])
        for i in range(len(height)):
            val = min(max_left[i], max_right[i]) - height[i]
            res += max(0, val)
        return res

class SolutionNeetcode:
    """
    time complexity: O(n)
    space complexity: O(1)
    """"
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


    def trap(self, height):
        """
        https://leetcode.com/problems/trapping-rain-water/solutions/17528/easy-to-understand-python-10-line-60ms-o-n/?orderBy=most_votes
        """
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterLevel += [left]  # over-fill it to left max height
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h  # drain to the right height
        return sum(waterLevel)
