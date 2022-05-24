# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkPath(self,node,targetSum,currSum):
        if node==None:
            return False
        if node.left==None and node.right==None and currSum+node.val==targetSum:
            return True
        return self.checkPath(node.left,targetSum,currSum+node.val) or self.checkPath(node.right,targetSum,currSum+node.val)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        return self.checkPath(root,targetSum,0)
        