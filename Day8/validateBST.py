import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validity(self,node,minVal,maxVal):
        if node==None:
            return True
        if node.val<=minVal or node.val>=maxVal:
            return False
        return self.validity(node.left,minVal,node.val) and self.validity(node.right,node.val,maxVal)
        
        
    def isValidBST(self, root):
        minVal = -9223372036854775807
        maxVal = 9223372036854775807
        return self.validity(root,minVal,maxVal)