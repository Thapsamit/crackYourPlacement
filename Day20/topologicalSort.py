class Solution:
    def topological(self,adj,i,vis,st):
        vis[i] = True
        for k in adj[i]:
            if not(vis[k]):
                self.topological(adj,k,vis,st)
        st.append(i)
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        st = []
        ans = []
        vis = [False for i in range(V)]
        for i in range(0,V,1):
            if not(vis[i]):
                self.topological(adj,i,vis,st)
        while len(st)!=0:
            x = st[-1]
            st.pop()
            ans.append(x)
        return ans