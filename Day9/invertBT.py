# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self,node):
        if node==None:
            return 
    
        temp = node.right
        node.right = node.left
        node.left = temp
        self.invert(node.left)
        self.invert(node.right)
        
    def invertTree(self, root):
        if root==None:
            return
        self.invert(root)
        return root