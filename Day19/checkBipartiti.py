class Solution:
    def checkBipartite(self,adj,V,i,col):
        qu = []
        qu.append(i)
        while len(qu)!=0:
            popped = qu.pop(0)
            for j in adj[popped]:
                if col[j]==-1:
                    col[j] = 1-col[popped]
                    qu.append(j)
                elif col[j]==col[popped]:
                    return False
        return True
	def isBipartite(self, V, adj):
	    col = [-1 for i in range(V)]
	    for i in range(0,V,1):
	        if col[i]==-1:
	            if not(self.checkBipartite(adj,V,i,col)):
	                return False
	    return True