def bstNodes(self,node,low,high,tNodes):
        if node==None:
            return 0
        if node.data>=low and node.data<=high:
            tNodes[0]+=1
        if node.data>low:
            self.bstNodes(node.left,low,high,tNodes)
        if node.data<=high:
            self.bstNodes(node.right,low,high,tNodes)
    def getCount(self,root,low,high):
        if root==None:
            return 0
        tNodes = [0]
        self.bstNodes(root,low,high,tNodes)
        return tNodes[0]