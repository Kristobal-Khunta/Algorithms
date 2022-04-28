# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return (
                [root.val]
                + self.preorderTraversal(root.left)
                + self.preorderTraversal(root.right)
            )

    def preorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:

            node = stack.pop()
            if node:
                ret.append(node.val)
                # вверху будет левое, потому что добавили позднее
                stack.append(node.right)
                stack.append(node.left)

        return ret

    def inorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def postorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            self.postorderTraversal(root.left)
            + self.postorderTraversal(root.right)
            + [root.val]
        )

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        while stack:

            node = stack.pop()
            if node:
                ret.append(node.val)
                # вверху будет левое, потому что добавили позднее
                stack.append(node.left)
                stack.append(node.right)

        return ret[::-1]
