# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxHeight(self,maxHeight,node):
        if node==None:
            return 0
        lh = self.maxHeight(maxHeight,node.left)
        lr = self.maxHeight(maxHeight,node.right)
        maxHeight = max(maxHeight,1+(max(lh,lr)))
        return maxHeight
    def maxDepth(self, root):
        if root==None:
            return 0
        maxHeight = 0
        mh = self.maxHeight(maxHeight,root)
        return mh
        
        