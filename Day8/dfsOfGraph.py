def fDfs(self,i,V,adj,dfs,vis):
        dfs.append(i)
        vis[i] = 1
        for j in adj[i]:
            if not(vis[j]):
                self.fDfs(j,V,adj,dfs,vis)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs = []
        vis = [0 for i in range(0,V,1)]
        for i in range(0,V,1):
            if not(vis[i]):
                self.fDfs(i,V,adj,dfs,vis)
        return dfs