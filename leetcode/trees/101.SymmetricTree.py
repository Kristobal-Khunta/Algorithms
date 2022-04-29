# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
         self.right = right
class Solution:
    def helper(self, path1, path2):
        if path1 is None and path2 is None:
            return True
        elif path1 is None or path2 is None:
            return False
        elif path1.val != path2.val:
            return False
        left_sym = self.helper(path1.left, path2.right)
        right_sym = self.helper(path1.right, path2.left)
        return left_sym & right_sym

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper(root.left, root.right)


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False
