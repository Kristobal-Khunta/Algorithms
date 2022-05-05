"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/discuss/516735/Python-2-solutions:-BFS-Iterative-O(1)-in-Space-Clean-and-Concise
    def linkNode(self, node):
        if node == None:
            return
        if self.leftMost == None:
            self.leftMost = node

        if self.prev != None:
            self.prev.next = node
        self.prev = node

    def connect(self, root: "Node") -> "Node":
        if root == None:
            return None
        self.leftMost = root
        while self.leftMost:
            head = self.leftMost
            self.leftMost = self.prev = None
            while head != None:  # Base on the above level
                self.linkNode(head.left)  # Try to link nodes on the current level
                self.linkNode(head.right)  # Try to link nodes on the current level
                head = head.next
        return root

    def connect(self, root: "Node") -> "Node":
        # https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/discuss/389389/Simply-Simple-Python-Solutions-Level-order-traversal-and-O(1)-space-both-approach
        dummy = Node(-1, None, None, None)
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None

        return res
