from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def markParents(self,node,parentNodes):
        qu = []
        qu.append(node)
        while len(qu)!=0:
            nd = qu[0]
            qu.pop(0)
            if nd.left:
                parentNodes[nd.left] = nd
                qu.append(nd.left)
            if nd.right:
                parentNodes[nd.right] = nd
                qu.append(nd.right)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentNodes = defaultdict(lambda:0)
        self.markParents(root,parentNodes)
        vis = defaultdict(lambda:0)
        qu = []
        qu.append(target)
        lev = 0
        vis[target] = True
        while len(qu)!=0:
            quSize = len(qu)
            if lev==k:
                break
            else:
                lev+=1
                for i in range(0,quSize,1):
                    curr = qu[0]
                    qu.pop(0)
                    if curr.left and vis[curr.left]!=True:
                        qu.append(curr.left)
                        vis[curr.left] = True
                    if curr.right and vis[curr.right]!=True:
                        qu.append(curr.right)
                        vis[curr.right] = True
                    if parentNodes[curr] and vis[parentNodes[curr]]!=True:
                        qu.append(parentNodes[curr])
                        vis[parentNodes[curr]] = True
        res = []
        while len(qu)!=0:
            curr = qu[0]
            qu.pop(0)
            res.append(curr.val)
        return res