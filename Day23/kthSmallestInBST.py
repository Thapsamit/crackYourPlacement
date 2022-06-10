# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root
        ans = 0
        while curr!=None or len(st)!=0:
            while curr!=None:
                st.append(curr)
                curr = curr.left  
            curr = st[-1]
            st.pop()
            ans+=1
            if ans==k:
                return curr.val
            curr = curr.right
        
        