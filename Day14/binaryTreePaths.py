# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bPaths(self,root,path,ans):
        if root==None:
            return 
        if root.left==None and root.right==None:
            path=path+str(root.val)
            ans.append(path)
            return 
        self.bPaths(root.left,path+str(root.val)+"->",ans)
        self.bPaths(root.right,path+str(root.val)+"->",ans)
    def binaryTreePaths(self, root):
        path = ""
        ans = []
        self.bPaths(root,path,ans)
        return ans
        