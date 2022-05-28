# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkSub(self,mainNode,subNode):
        if mainNode==None and subNode==None:
            return True
        if mainNode==None or subNode==None:
            return False
        return mainNode.val==subNode.val and self.checkSub(mainNode.left,subNode.left) and self.checkSub(mainNode.right,subNode.right)
    def isSubtree(self, root, subRoot):
        if root==None or subRoot==None:
            return False
        if self.checkSub(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        