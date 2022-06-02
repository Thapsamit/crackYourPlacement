# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,path,minAbs):
        if node==None:
            return 
        self.inorder(node.left,path,minAbs)
        if len(path)!=0:
            minAbs[0]=min(minAbs[0],abs(node.val-path[-1]))
        path.append(node.val)
        self.inorder(node.right,path,minAbs)
    def getMinimumDifference(self, root):
        if root==None:
            return 
        path = []
        minAbs = [999999999]
        self.inorder(root,path,minAbs)
        return minAbs[0]