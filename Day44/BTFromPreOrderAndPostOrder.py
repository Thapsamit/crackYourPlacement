# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def binaryTree(self,preorder,postorder,preS,preE,postS,postE):
        if preS>preE:
            return None
        node = TreeNode(preorder[preS])
        if preS==preE:
            return node
        idx = postS
        while postorder[idx]!=preorder[preS+1]:
            idx+=1
        leftEle = idx-postS+1
    
        node.left = self.binaryTree(preorder,postorder,preS+1,preS+leftEle,postS,idx)
        node.right = self.binaryTree(preorder,postorder,preS+leftEle+1,preE,idx+1,postE-1)
        return node
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root = self.binaryTree(preorder,postorder,0,n-1,0,n-1)
        return root
        
        