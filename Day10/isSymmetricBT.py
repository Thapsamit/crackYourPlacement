# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self,leftNode,rightNode):
        if leftNode==None or rightNode==None:
            return leftNode==rightNode
        if leftNode.val!=rightNode.val:
            return False
        return self.checkSymmetry(leftNode.left,rightNode.right) and self.checkSymmetry(leftNode.right,rightNode.left)
            
            
    def isSymmetric(self, root):
        if root==None:
            return 
        return self.checkSymmetry(root.left,root.right)
        