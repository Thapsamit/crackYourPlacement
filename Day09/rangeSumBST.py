# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRange(self,node,low,high,total):
        if node==None:
            return 
        if node.val>=low and node.val<=high:
            total[0]+=node.val
            self.findRange(node.left,low,high,total)
            self.findRange(node.right,low,high,total)
        elif node.val<low:
            self.findRange(node.right,low,high,total)
        else:
            self.findRange(node.left,low,high,total)
    def rangeSumBST(self, root, low, high):
        if root==None:
            return 0
        total = [0]
        self.findRange(root,low,high,total)
        return total[0]
        