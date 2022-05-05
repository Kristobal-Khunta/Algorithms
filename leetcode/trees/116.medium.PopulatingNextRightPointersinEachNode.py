# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/discuss/1654181/C++PythonJava-Simple-Solution-w-Images-and-Explanation-or-BFS-+-DFS-+-O(1)-Optimized-BFS
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

