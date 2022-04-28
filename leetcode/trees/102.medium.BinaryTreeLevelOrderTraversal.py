# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        res_lvl = []
        curr = root
        lvl = 0
        while curr or queue:
            if curr:
                res_lvl.append(curr.val)
                queue.append((curr.left, lvl + 1))
                queue.append((curr.right, lvl + 1))
            curr, new_lvl = queue.pop(0)
            if new_lvl > lvl:
                res.append(res_lvl)
                res_lvl = []
                lvl = new_lvl
        return res

from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), []
        
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res