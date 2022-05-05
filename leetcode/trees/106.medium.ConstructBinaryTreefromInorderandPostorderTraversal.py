# Given two integer arrays inorder and postorder
# where inorder is the inorder traversal of a binary tree
#  and postorder is the postorder traversal of the same tree,
#  construct and return the binary tree.

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # explanatio solutio https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/1589310/C%2B%2BPython-2-Simple-Solutions-w-Images-and-Detailed-Explanation-or-Recursion-%2B-Hashmap
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {val: i for i, val in enumerate(inorder)}

        def recur(low, high):
            if low > high:
                return None
            val = postorder.pop()
            mid = map_inorder[val]
            node = TreeNode(val)
            node.right = recur(mid + 1, high)
            node.left = recur(low, mid - 1)
            return node

        return recur(0, len(inorder) - 1)
