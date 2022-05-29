class Solution:
    def isCyclic(self,i,adj,V,vis):
        qu = []
        qu.append(i)
        while len(qu)!=0:
            ver = qu.pop(0)
            if vis[ver]==True:
                return True
            vis[ver] = True
            for j in adj[ver]:
                if vis[j]==False:
                    qu.append(j)
        return False
        
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        vis = [False for i in range(V)]
        for i in range(0,V,1):
            if vis[i]==False:
                if(self.isCyclic(i,adj,V,vis)):
                    return True
        return False