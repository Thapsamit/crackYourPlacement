from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        lev = 1
        qu = deque()
        qu.append(root)
        ans = [[root.val]]
        while len(qu)!=0:
            tSize = len(qu)
            group = []
            for i in range(0,tSize,1):
                if lev%2!=0:
                    node = qu[0]
                    qu.popleft()
                    if node.right!=None:
                        qu.append(node.right)
                        group.append(node.right.val)
                    if node.left!=None:
                        qu.append(node.left)
                        group.append(node.left.val)
                else:
                    node = qu[-1]
                    qu.pop()
                    if node.left!=None:
                        qu.appendleft(node.left)
                        group.append(node.left.val)
                    if node.right!=None:
                        qu.appendleft(node.right)
                        group.append(node.right.val)
            lev+=1
            if len(group)!=0:
                ans.append(group)
        return ans
                    
                
                
        