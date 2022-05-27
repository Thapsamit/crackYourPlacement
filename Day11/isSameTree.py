# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSame(self,node1,node2):
        if node1==None and node2==None:
            return True
        if node1==None or node2==None:
            return False
        if node1.val!=node2.val:
            return False
        return self.checkSame(node1.left,node2.left) and self.checkSame(node1.right,node2.right)
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return self.checkSame(p,q)
        