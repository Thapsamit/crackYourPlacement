# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node):
        if node==None:
            return 0
        return max(self.height(node.left),self.height(node.right))+1
    def isBalanced(self, root):
        if root==None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left)==True and self.isBalanced(root.right)==True:
            return True
        return False
        