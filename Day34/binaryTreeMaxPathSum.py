# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumPathSum(self,node,maxVal):
        if node==None:
            return 0
        lSum = max(0,self.maximumPathSum(node.left,maxVal))
        rSum = max(0,self.maximumPathSum(node.right,maxVal))
        maxVal[0] = max(maxVal[0],node.val+lSum+rSum)
        return node.val+max(lSum,rSum)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [-99999999]
        self.maximumPathSum(root,maxVal)
        return maxVal[0]
        