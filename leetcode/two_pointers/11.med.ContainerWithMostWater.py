class Solution:
    """
    proofs:
    1) https://leetcode.com/problems/container-with-most-water/solutions/6089/Anyone-who-has-a-O(N)-algorithm/comments/7268/
    2) https://leetcode.com/problems/container-with-most-water/solutions/127443/container-with-most-water/?orderBy=most_votes
    """

    def maxArea(self, height: List[int]) -> int:
        max_square = 0
        left, right = 0, len(height) - 1
        while left < right:
            square = (right - left) * min(height[left], height[right])
            max_square = max(square, max_square)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_square
