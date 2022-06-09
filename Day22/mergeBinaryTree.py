# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merging(self,root1,root2):
        if root1==None and root2==None:
            return None
        elif root1!=None and root2!=None:
            node = TreeNode(root1.val+root2.val)
            node.left = self.merging(root1.left,root2.left)
            node.right = self.merging(root1.right,root2.right)
        elif root1!=None or root2!=None:
            if root1!=None:
                node = TreeNode(root1.val)
                node.left = self.merging(root1.left,root2)
                node.right = self.merging(root1.right,root2)
            else:
                node = TreeNode(root2.val)
                node.left = self.merging(root1,root2.left)
                node.right = self.merging(root1,root2.right)
        return node
        
        
                
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None and root2==None:
            return None
        if root1==None:
            return root2
        if root2==None:
            return root1
        newRoot = self.merging(root1,root2)
        return newRoot