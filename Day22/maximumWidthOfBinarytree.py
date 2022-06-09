# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        qu = []
        qu.append([root,0])
        maxWidth = 0
        while len(qu)!=0:
            tSize = len(qu)
            mmin = qu[0][1]
            for i in range(0,tSize,1):
                curr = qu[0][1]-mmin
                node = qu[0][0]
                qu.pop(0)
                if i==0:
                    first = curr
                if i==tSize-1:
                    last = curr
                if node.left!=None:
                    qu.append([node.left,curr*2+1])
                if node.right!=None:
                    qu.append([node.right,curr*2+2])
        
            maxWidth = max(maxWidth,last-first+1)
            
        return maxWidth
            