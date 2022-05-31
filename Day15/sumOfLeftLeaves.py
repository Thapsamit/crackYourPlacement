# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def sumLeft(self,node,haveLeft,total):
        if node==None:
            return 
        if node.left==None and node.right==None and haveLeft==1:
            total[0]+=node.val
        self.sumLeft(node.left,1,total)
        self.sumLeft(node.right,0,total)
    def sumOfLeftLeaves(self, root):
        if root==None or (root.left==None and root.right==None):
            return 0
        total = [0]
        haveLeft = 0
        self.sumLeft(root,haveLeft,total)
        return total[0]
        
        