class Solution:
    def findInorder(self,node,ans):
        if node==None:
            return 
        self.findInorder(node.left,ans)
        ans.append(node.val)
        self.findInorder(node.right,ans)
        
    def inorderTraversal(self, root):
        ans = []
        self.findInorder(root,ans)
        return ans
        