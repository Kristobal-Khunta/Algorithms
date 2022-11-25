# TASK:
# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/discuss/929000/Recursive-solution-long-explanation
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:  # edge case, see exposition below
            return [None]

        all_trees = []  # list of all unique BSTs
        for curRootVal in range(
            start, end + 1
        ):  # generate all roots using list [start, end]
            # recursively get list of subtrees less than curRoot (a BST must have left subtrees less than the root)
            all_left_subtrees = self.helper(start, curRootVal - 1)

            # recursively get list of subtrees greater than curRoot (a BST must have right subtrees greater than the root)
            all_right_subtrees = self.helper(curRootVal + 1, end)

            for left_subtree in all_left_subtrees:  # get each possible left subtree
                for (
                    right_subtree
                ) in all_right_subtrees:  # get each possible right subtree
                    # create root node with each combination of left and right subtrees
                    curRoot = TreeNode(curRootVal)
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree

                    # curRoot is now the root of a BST
                    all_trees.append(curRoot)

        return all_trees


class Solution:
    # [Python] DFS with Memoization - Clean & Concise
    # https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/discuss/1440128/Python-DFS-with-Memoization-Clean-and-Concise
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            ans = []
            for root in range(left, right + 1):
                leftNodes = dfs(left, root - 1)
                rightNodes = dfs(root + 1, right)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        ans.append(rootNode)
            return ans

        return dfs(1, n)
