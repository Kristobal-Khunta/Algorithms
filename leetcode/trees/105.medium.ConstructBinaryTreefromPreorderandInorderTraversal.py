# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {val: i for i, val in enumerate(inorder)}
        preorder = preorder[::-1]

        def recur(low, high):
            if low > high:
                return None
            val = preorder.pop()
            mid = map_inorder[val]
            node = TreeNode(val)
            node.left = recur(low, mid - 1)
            node.right = recur(mid + 1, high)

            return node

        return recur(0, len(inorder) - 1)


class Solution:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {val: i for i, val in enumerate(inorder)}
        cur_idx = 0

        def recur(low, high):
            nonlocal cur_idx
            if low > high:
                return None
            val = preorder[cur_idx]
            cur_idx += 1
            mid = map_inorder[val]
            node = TreeNode(val)
            node.left = recur(low, mid - 1)
            node.right = recur(mid + 1, high)

            return node

        return recur(0, len(inorder) - 1)
