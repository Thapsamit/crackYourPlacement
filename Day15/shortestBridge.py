class Solution:
    def dfs(self,grid,i,j,qu,nb,vis):
        vis[i][j] = 1
        qu.append([i,j])
        for k in range(0,4,1):
            di = i+nb[k][0]
            dj = j+nb[k][1]
            if di>=0 and dj>=0 and di<len(grid) and dj<len(grid) and vis[di][dj]==0 and grid[di][dj]==1:
                self.dfs(grid,di,dj,qu,nb,vis)
    def shortestBridge(self, grid):
        m = len(grid)
        n = len(grid[0])
        qu = []
        nb = [[-1,0],[1,0],[0,1],[0,-1]]
        vis = [[0 for i in range(m)] for j in range(n)]
        flag = False
        for i in range(0,m,1):
            for j in range(0,n,1):
                if grid[i][j]==1:
                    self.dfs(grid,i,j,qu,nb,vis)
                    flag = True
                    break
            if flag==True:
                break
        lev = 0
        while len(qu)!=0:
            si = len(qu)
            for p in range(0,si,1):
                rem = qu.pop(0)
                for s in range(0,4,1):
                    di = rem[0]+nb[s][0]
                    dj = rem[1]+nb[s][1]
                    if di<0 or dj<0 or di>=m or dj>=n or vis[di][dj]==1:
                        continue
                    if grid[di][dj]==1:
                        return lev
                    qu.append([di,dj])
                    vis[di][dj] = 1
            lev+=1
        return lev
                
                
                
                
                
                
                
                
                
                
                
            
        