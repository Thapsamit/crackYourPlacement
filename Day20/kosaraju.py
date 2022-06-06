class Solution:
    def topological(self,adj,i,vis,st):
        vis[i] = True
        for k in adj[i]:
            if not(vis[k]):
                self.topological(adj,k,vis,st)
        st.append(i)
    def reverseDfs(self,reversedAdj,x,vis):
        vis[x] = True
        for k in reversedAdj[x]:
            if not(vis[k]):
                self.reverseDfs(reversedAdj,k,vis)
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        st = []
        totalSc = 0
        vis = [False for i in range(V)]
        for i in range(0,V,1):
            if not(vis[i]):
                self.topological(adj,i,vis,st)
        reversedAdj = []
        for i in range(0,V,1):
            vis[i] = False
            reversedAdj.append([])
        for i in range(0,V,1):
            for s in adj[i]:
                reversedAdj[s].append(i)
        while len(st)!=0:
            x = st[-1]
            st.pop()
            if not(vis[x]):
                self.reverseDfs(reversedAdj,x,vis)
                totalSc+=1
        return totalSc