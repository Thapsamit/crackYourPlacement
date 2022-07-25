class Solution:
    def findNodeToRootPath(self,node,path,data):
        if node==None:
            return False
        if node.data==data:
            path.append(node.data)
            return True
        inLeft = self.findNodeToRootPath(node.left,path,data)
        if(inLeft):
            path.append(node.data)
            return True
        inRight = self.findNodeToRootPath(node.right,path,data)
        if(inRight):
            path.append(node.data)
            return True
        return False
    def findDist(self,root,a,b):
        p1 = [] #path of a
        p2 = [] #path of b
       
        self.findNodeToRootPath(root,p1,a)
        self.findNodeToRootPath(root,p2,b)
       
        i = len(p1)-1
        j = len(p2)-1
        while i>=0 and j>=0 and p1[i]==p2[j]:
            i-=1
            j-=1 
        i+=1 #find lca index
        j+=1 #find lca index
        return (i+j)