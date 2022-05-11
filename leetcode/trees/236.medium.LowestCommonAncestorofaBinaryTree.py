class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def recursive(self, currentNode: "TreeNode", p: "TreeNode", q: "TreeNode"):
        if currentNode is None:
            return False
        mid = currentNode == p or currentNode == q
        left = self.recursive(currentNode.left, p, q)
        right = self.recursive(currentNode.right, p, q)
        if (mid + left + right >= 2) and self.ans is None:
            self.ans = currentNode
        return mid or left or right

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.recursive(root, p, q)
        return self.ans


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None
        left_res = self.lowestCommonAncestor(root.right, p, q)
        right_res = self.lowestCommonAncestor(root.left, p, q)
        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If looking for me, return myself
        if root == p or root == q:
            return root

        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            return left or right


class Solution:
    """
    https://leetcode.com/problems/
    lowest-common-ancestor-of-a-binary-tree/discuss/
    152682/Python-simple-recursive-solution-with-detailed-explanation

    There's a design that needs to think about:

    For lowestCommonAncestor(node,p,q),
    what if p and q do not both exist? what it will return?
    The solution is as the author did:
    if only one of them exists, say p,
    then it will return p ( which is Lowest Ancestor of p;
    -> nothing to do with LCA !)
    if non of them exists, it will return None

    For me, I feel code in this way delivers the idea more clearly:
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def findLowestAncestor(root, p, q):
            """
            return: TreeNode,
                it can be LOWEST ancestor of: p, or q, or both.
                    if it's lowest ancestor of only p -> it should be p itself
                    if it's lowest ancestor of only q -> it should be q itself
            """
            if not root:
                return None
            if root == p or root == q:
                return root
            left_LA = findLowestAncestor(root.left, p, q)
            right_LA = findLowestAncestor(root.right, p, q)

            if left_LA and right_LA:
                return root
            if left_LA and not right_LA:
                return left_LA
            if right_LA and not left_LA:
                return right_LA

        # This function is just 'LA', not necessary to be 'LCA';
        # but, because in this problem,  p and q are guranteed in the tree
        # what we get will be LA of both p and q, i.e. LCA.
        LCA = findLowestAncestor(root, p, q)
        return LCA
