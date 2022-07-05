# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getBst(self,nums,l,r):
        if l>r:
            return None
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.getBst(nums,l,mid-1)
        root.right = self.getBst(nums,mid+1,r)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getBst(nums,0,len(nums)-1)
        