# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# UPVOTE if you like (🌸◠‿◠), If you have any question, feel free to ask.

# To calculate the maximum depth we can use the Depth-First Search.
#  We call a helper function recursively and return
#  the maximum depth between left and right branches.

# Time: O(N) - for DFS
# Space: O(N) - for the recursive stack

# Runtime: 40 ms, faster than 89.54% of Python3
# online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 18.15% of
# Python3 online submissions for Maximum Depth of Binary Tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)
