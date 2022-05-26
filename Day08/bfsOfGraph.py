def bfsOfGraph(self, V, adj):
        bfs = []
        vis = []
        qu = []
        qu.append(0)
        vis.append(0)
        while len(qu)!=0:
            n = qu.pop(0)
            bfs.append(n)
            for j in adj[n]:
                if j not in vis:
                    vis.append(j)
                    qu.append(j)
        return bfs