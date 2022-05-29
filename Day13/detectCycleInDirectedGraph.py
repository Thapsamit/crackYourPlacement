class Solution:
    def checkCycle(self,idx,adj,vis,dfsVis,V):
        vis[idx] = True
        dfsVis[idx] = True
        for n in adj[idx]:
            if vis[n]==False:
                if self.checkCycle(n,adj,vis,dfsVis,V):
                    return True
            elif dfsVis[n]==True:
                return True
        dfsVis[idx] = False
        return False
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis = [False for i in range(V)]
        dfsVis = [False for i in range(V)]
        for i in range(0,V,1):
            if vis[i]==False:
                if(self.checkCycle(i,adj,vis,dfsVis,V)):
                    return True
        return False