# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        qu = []
        ans = []
        if root==None:
            return ans
        qu.append(root)
        while len(qu)!=0:
            temp = []
            totalEle = len(qu)
            s = 0
            while s<totalEle:
                popped = qu.pop(0)
                temp.append(popped.val)
                if popped.left!=None:
                    qu.append(popped.left)
                if popped.right!=None:
                    qu.append(popped.right)
                s+=1
            ans.append(temp)
        return ans
        