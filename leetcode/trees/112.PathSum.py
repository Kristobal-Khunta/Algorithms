# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], prevSum: int, targetSum: int):
        curSum = prevSum+root.val
        if root.left is None and root.right is None: 
            
            return curSum == targetSum
        
        left_side = right_side = False
        if root.left:
            left_side = self.helper(root.left, curSum, targetSum)
        if root.right:
            right_side = self.helper(root.right, curSum, targetSum)
        return left_side or right_side
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.helper(root,0,targetSum)


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)