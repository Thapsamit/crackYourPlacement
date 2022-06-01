# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        st = []
        if root!=None:
            st.append(root)
        while len(st)!=0:
            node = st.pop()
            if node.right!=None:
                st.append(node.right)
            if node.left!=None:
                st.append(node.left)
            if len(st)!=0:
                node.right = st[-1]
            node.left = None
            
        """
        Do not return anything, modify root in-place instead.
        """
        