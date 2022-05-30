# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root, p, q):
        if root==None or p.val==root.val or q.val==root.val:
            return root
        lp = self.lowestCommonAncestor(root.left,p,q)
        lq = self.lowestCommonAncestor(root.right,p,q)
        if lp==None:
            if lq!=None:
                return lq
        elif lq==None:
            if lp!=None:
                return lp
        else:
            return root
        
        
        